import os
import dill as pkl
import warnings
from packaging import version
import h5py
import json

import jax.numpy as jnp
import numpy as np
import jax
from jax import lax, vmap

from starred.utils.generic_utils import (pad_and_convolve, pad_and_convolve_fft, fwhm2sigma, gaussian_function,
    make_grid, gaussian_function_batched,
    moffat_elliptical_function, moffat_function, Downsample, scipy_convolve, save_npy, save_fits,
    convert_numpy_array_to_list, convert_list_to_numpy_array)


class PSF(object):
    """
    Narrow Point Spread Function class. Coordinates and FWHM are given in the original pixel grid.

    """

    def __init__(
            self,
            image_size=64,
            number_of_sources=2,
            upsampling_factor=2,
            gaussian_fwhm=2,
            convolution_method='scipy',
            gaussian_kernel_size=None,
            include_moffat=True,
            elliptical_moffat=False,
    ):
        """
        :param image_size: input images size in pixels
        :type image_size: int
        :param number_of_sources: number of input images (each containing a point source)
        :type number_of_sources: int
        :param upsampling_factor: the rate at which the sampling frequency increases in the PSF with respect to the input images
        :type upsampling_factor: int
        :param gaussian_fwhm: the Gaussian's FWHM in pixels. Default is 2.
        :type gaussian_fwhm: int
        :param convolution_method: method to use to calculate the convolution, choose between 'fft', 'scipy', and 'lax. Recommended if jax>=0.4.9 : 'scipy'
        :type convolution_method: str
        :param gaussian_kernel_size: dimensions of the Gaussian kernel, not used if method = 'fft'. None will select the recommended size for each method.
        :type gaussian_kernel_size: int
        :param include_moffat: True for the PSF to be expressed as the sum of a Moffat and a grid of pixels. False to not include the Moffat. Default: True
        :type include_moffat: bool
        :param elliptical_moffat: Allow elliptical Moffat.
        :type elliptical_moffat: bool

        """
        self.elliptical_moffat = elliptical_moffat
        if self.elliptical_moffat:
            self.analytic = self._analytic_ellitpical
        else:
            self.analytic = self._analytic_circular

        self.image_size = image_size
        self.upsampling_factor = upsampling_factor
        self.image_size_up = self.image_size * self.upsampling_factor
        self.M = number_of_sources
        self.include_moffat = include_moffat

        if convolution_method == 'fft':
            self._convolve = pad_and_convolve_fft
            self.gaussian_size = self.image_size_up
            if (self.image_size * self.upsampling_factor) % 2 == 1:
                self.shift_gaussian = 0.
            else :
                self.shift_gaussian = 0.5 #convention for even kernel size and fft convolution
            self.shift_direction = 1.
        elif convolution_method == 'lax':
            self._convolve = pad_and_convolve
            if gaussian_kernel_size is None:
                self.gaussian_size = 12
            else:
                self.gaussian_size = gaussian_kernel_size
            self.shift_gaussian = 0.5
            self.shift_direction = 1.
        elif convolution_method == 'scipy':
            self._convolve = scipy_convolve
            if gaussian_kernel_size is None:
                self.gaussian_size = 16
            else:
                self.gaussian_size = gaussian_kernel_size
            if version.parse(jax.__version__) < version.parse('0.4.9'):
                warnings.warn("WARNING : jax.scipy has no FFT implementation for the moment. It might be faster to use 'fft' on CPU.")

            self.shift_gaussian = 0.5
            self.shift_direction = -1 #scipy has inverted shift convention
        else:
            raise NotImplementedError('Unknown convolution method : choose fft, scipy or lax')

        self.convolution_method = convolution_method
        self.fwhm = gaussian_fwhm
        self.sigma = fwhm2sigma(self.fwhm)

    def shifted_gaussians(self, i, x0, y0):
        """
        Generates a 2D array with point sources. Normalized to 1.

        :param i: current point source index
        :type i: int
        :param x0: 1D array containing the x positions of the point sources, shift are given in unit of 'big' pixels
        :param y0: 1D array containing the y positions of the point sources, shift are given in unit of 'big' pixels
        :return: 2D array

        """
        x, y = make_grid(numPix=self.gaussian_size, deltapix=1.)
        return jnp.array(gaussian_function(
            x=x, y=y,
            amp=1, sigma_x=self.sigma,
            sigma_y=self.sigma,
            center_x=-(self.upsampling_factor * x0[i])*self.shift_direction - self.shift_gaussian,
            center_y=-(self.upsampling_factor * y0[i])*self.shift_direction - self.shift_gaussian,  # Convention : gaussian is placed at a center of a pixel
        ).reshape(self.gaussian_size, self.gaussian_size))

    def shifted_gaussians_vectorized(self, x0, y0):
        """
        shifted_gaussian method above vectorized over 'i' using broadcasting.
        """
        x, y = make_grid(numPix=self.gaussian_size, deltapix=1.)
        center_x = -(self.upsampling_factor * x0) * self.shift_direction - self.shift_gaussian
        center_y = -(self.upsampling_factor * y0) * self.shift_direction - self.shift_gaussian
        gaussian_batches = gaussian_function_batched(
            x, y,
            amp=jnp.ones_like(x0),
            sigma_x=self.sigma,
            sigma_y=self.sigma,
            center_x=center_x,
            center_y=center_y,
        ).reshape(len(x0), self.gaussian_size, self.gaussian_size)
        return gaussian_batches  # 3D array, len(x0) slices.

    def _analytic_ellitpical(self, fwhmx, fwhmy, phi, beta):
        """
        Generates the narrow PSF's analytic term.

        :param fwhm_x: the full width at half maximum value in the x direction
        :type fwhm_x: float
        :param fwhm_y: the full width at half maximum value in the y direction
        :type fwhm_y: float
        :param phi: orientation angle
        :type phi: float
        :param beta: the Moffat beta parameter
        :type beta: float

        :return: 2D Moffat

        """
        x, y = make_grid(numPix=self.image_size_up, deltapix=1.)
        return jnp.array(moffat_elliptical_function(
            x=x, y=y,
            amp=1, fwhm_x=fwhmx * self.upsampling_factor,
            fwhm_y = fwhmy * self.upsampling_factor, phi=phi, beta=beta,
            center_x=0,
            center_y=-0,
        ).reshape(self.image_size_up, self.image_size_up))

    def _analytic_circular(self, fwhm, beta):
        """
        Generates the narrow PSF's analytic term.

        :param fwhm: the full width at half maximum value in the x direction
        :type fwhm: float
        :param beta: the Moffat beta parameter
        :type beta: float

        :return: 2D Moffat

        """
        x, y = make_grid(numPix=self.image_size_up, deltapix=1.)
        return jnp.array(moffat_function(
            x=x, y=y,
            amp=1, fwhm=fwhm * self.upsampling_factor,
            beta=beta,
            center_x=0,
            center_y=-0,
        ).reshape(self.image_size_up, self.image_size_up))

    # @partial(jit, static_argnums=(0, 1, 5))
    def model(self, kwargs_moffat=None, kwargs_gaussian=None, kwargs_background=None, high_res=False):
        """
        Creates the 2D narrow Point Spread Function (PSF) image.

        :param init: stamp index
        :type init: int
        :param kwargs_moffat: dictionary containing keyword arguments corresponding to the analytic term of the PSF
        :param kwargs_gaussian: dictionary containing keyword arguments corresponding to the Gaussian deconvolution kernel
        :param kwargs_background: dictionary containing keyword arguments corresponding to the grid of pixels
        :param high_res: returns the upsampled version of the PSF
        :type high_res: bool
        :return: array containing the model

        """

        s = self.get_narrow_psf(kwargs_moffat, kwargs_gaussian, kwargs_background, norm=False)
        # s is a 2d array
        r = self.get_gaussians_vectorized(kwargs_gaussian, kwargs_moffat)
        # r is a 3d array.
        # so we need to adapt our _convolve function. the first argument (s) will be batched over the slices
        # of r:
        convolve_batched = vmap(self._convolve, in_axes=(None, 0))
        # okay let's convolve
        model = convolve_batched(s, r)
        if not high_res:
            # we also need to vectorize downsample ...
            downsample_batched = vmap(lambda x: Downsample(x, factor=self.upsampling_factor),
                                      in_axes=(0,))
            model = downsample_batched(model)
        return model

    def get_moffat(self, kwargs_moffat, norm=True):
        """
        Returns the analytical part of the PSF.

        :param kwargs_moffat: dictionary containing keyword arguments corresponding to the analytic term of the PSF
        :param norm: normalizes the Moffat
        :type norm: bool

        """
        if self.elliptical_moffat:
            moff = kwargs_moffat['C'] * self.analytic(kwargs_moffat['fwhm_x'], kwargs_moffat['fwhm_y'],
                                                      kwargs_moffat['phi'], kwargs_moffat['beta'])
        else:
            moff = kwargs_moffat['C'] * self.analytic(kwargs_moffat['fwhm'], kwargs_moffat['beta'])
        if norm:
            moff = moff / moff.sum()

        return moff

    def get_narrow_psf(self, kwargs_moffat=None, kwargs_gaussian=None, kwargs_background=None, norm=True):
        """
        Returns the `narrow` PSF s.

        :param kwargs_moffat: dictionary containing keyword arguments corresponding to the analytic term of the PSF
        :param kwargs_background: dictionary containing keyword arguments corresponding to the grid of pixels
        :return: array containing the `narrow` PSF
        """

        background = self.get_background(kwargs_background)
        if self.include_moffat:
            moff = self.get_moffat(kwargs_moffat, norm=False)
            s = moff + background
        else:
            s = background
            moff = jnp.zeros_like(s)
            s += lax.cond(s.sum() == 0, lambda _: 1e-6, lambda _: 0., operand=None)  # to avoid division per 0

        if norm:
            s = s / s.sum()

        return s

    def get_full_psf(self, kwargs_moffat=None, kwargs_gaussian=None, kwargs_background=None, norm=True, high_res=True):
        """
        Returns the PSF of the original image, `i.e.`, the convolution between s, the `narrow` PSF, and r, the Gaussian kernel.

        :param kwargs_moffat: dictionary containing keyword arguments corresponding to the analytic term of the PSF
        :param kwargs_gaussian: dictionary containing keyword arguments corresponding to the Gaussian deconvolution kernel
        :param kwargs_background: dictionary containing keyword arguments corresponding to the grid of pixels
        :return: array containing the full PSF

        """
        s = self.get_narrow_psf(kwargs_moffat=kwargs_moffat, kwargs_gaussian=kwargs_gaussian, kwargs_background=kwargs_background, norm=norm)
        r = self.shifted_gaussians(0, [0.], [0.])
        if high_res:
            psf = self._convolve(s, r)
        else :
            psf = Downsample(self._convolve(s, r), factor=self.upsampling_factor)
        if norm:
            psf /= psf.sum()

        return psf

    def get_background(self, kwargs_background):
        """
        Returns the numerical part of the PSF.

        :param kwargs_background: dictionary containing keyword arguments corresponding to the grid of pixels
        :return: array containing the background correction
        """

        return kwargs_background['background'].reshape(self.image_size_up, self.image_size_up)

    def get_gaussian(self, init, kwargs_gaussian, kwargs_moffat):
        """
        Returns a Gaussian function, adjusted to the star of index ``init``.

        :param init: stamp index
        :type init: int
        :param kwargs_gaussian: dictionary containing keyword arguments corresponding to the Gaussian deconvolution kernel
        :return: array containing the Gaussian kernel
        """
        x0, y0 = kwargs_gaussian['x0'], kwargs_gaussian['y0']
        r = self.shifted_gaussians(init, x0, y0)

        # ga = kwargs_gaussian['a'][init] / jnp.mean(kwargs_gaussian['a']) #normalization by the mean to remove degeneracy with the C parameter of the moffat
        ga = kwargs_gaussian['a'][init] / kwargs_moffat[
            'C']  # normalization by the mean to remove degeneracy with the C parameter of the moffat
        r = ga * r

        return r

    def get_gaussians_vectorized(self, kwargs_gaussian, kwargs_moffat):
        """
        Same as get_gaussian, but doing all the slices at once.

        :param kwargs_gaussian: dictionary containing keyword arguments corresponding to the Gaussian deconvolution kernel
        :param kwargs_moffat: dictionary of the arguments of the Moffat. necessary for normalization purposes.

        :return: 2D array containing slices, each with Gaussian kernel at the positions given in kwargs_gaussian.
                 (so, slices of a flattened 2D array, hence 2D)
        """
        x0, y0 = kwargs_gaussian['x0'], kwargs_gaussian['y0']
        r = self.shifted_gaussians_vectorized(x0, y0)
        # this is a 3D array, stack of slices (one per position (x,y) of the arrays (x0, y0)).

        # normalization by the mean to remove degeneracy with the C parameter of the moffat
        ga = kwargs_gaussian['a'] / kwargs_moffat['C']
        r = ga[:, None, None] * r

        # so, we now have slices each containing a single gaussian, properly normalized, at the right position
        # in each slice.
        return r

    def get_amplitudes(self, kwargs_moffat=None, kwargs_gaussian=None, kwargs_background=None):
        """
        Returns the photometry of the stars.

        :param kwargs_moffat: dictionary containing keyword arguments corresponding to the analytic term of the PSF
        :param kwargs_gaussian: dictionary containing keyword arguments corresponding to the Gaussian deconvolution kernel
        :param kwargs_background: dictionary containing keyword arguments corresponding to the grid of pixels

        :return: list containing the relative photometry
       """

        kernel = self.get_narrow_psf(kwargs_moffat, kwargs_gaussian, kwargs_background, norm=False)
        kernel_norm = kernel.sum()
        amp = (kwargs_gaussian['a'] / kwargs_moffat['C']) * kernel_norm
        return amp

    def get_photometry(self, kwargs_moffat=None, kwargs_gaussian=None, kwargs_background=None, high_res=False):
        """
        Returns the PSF photometry of all the stars.

        :param kwargs_moffat: dictionary containing keyword arguments corresponding to the analytic term of the PSF
        :param kwargs_gaussian: dictionary containing keyword arguments corresponding to the Gaussian deconvolution kernel
        :param kwargs_background: dictionary containing keyword arguments corresponding to the grid of pixels.
        :return: array containing the photometry
        """
        model = self.model(kwargs_moffat, kwargs_gaussian, kwargs_background, high_res)
        return jnp.sum(model, axis=(1, 2))

    def get_astrometry(self, kwargs_moffat=None, kwargs_gaussian=None, kwargs_background=None):
        """
        Returns the astrometry. In units of 'big' pixel.

        :param kwargs_moffat: dictionary containing keyword arguments corresponding to the analytic term of the PSF
        :param kwargs_gaussian: dictionary containing keyword arguments corresponding to the Gaussian deconvolution kernel
        :param kwargs_background: dictionary containing keyword arguments corresponding to the grid of pixels

        :return: list of tuples with format [(x1,y1), (x2,y2), ...]
        """
        coord = []
        for x, y in zip(kwargs_gaussian['x0'], kwargs_gaussian['y0']):
            coord.append([x, y])

        return np.asarray(coord)

    def export(self, output_folder, kwargs_final, data, sigma_2, format='fits'):
        """
        Saves all the output files in fits or npy format.

        :param output_folder: path to the output folder
        :type output_folder: str
        :param kwargs_final: dictionary containing all keyword arguments
        :param data: array containing the images
        :param sigma_2: array containing the noise maps
        :param format: output format. Choose between ``npy`` or ``fits``
        :type format: str
        """
        if format == 'fits':
            save_fct = save_fits
        elif format == 'npy':
            save_fct = save_npy
        else:
            raise NotImplementedError(f'Format {format} unknown.')

        narrow = self.get_narrow_psf(**kwargs_final, norm=True)
        save_fct(narrow, os.path.join(output_folder, 'narrow_PSF'))

        full = self.get_full_psf(**kwargs_final, norm=True, high_res=True)
        save_fct(full, os.path.join(output_folder, 'full_PSF'))

        background = self.get_background(kwargs_final['kwargs_background'])
        save_fct(background, os.path.join(output_folder, 'background_PSF'))

        analytic = self.get_moffat(kwargs_final['kwargs_moffat'], norm=True)
        save_fct(analytic, os.path.join(output_folder, 'analytic_PSF'))

        estimated_full_psf = self.model(**kwargs_final)
        dif = data - estimated_full_psf
        rr = jnp.abs(dif) / jnp.sqrt(sigma_2)

        for i in range(self.M):
            save_fct(estimated_full_psf[i], os.path.join(output_folder, f'full_psf_{i}'))
            save_fct(dif[i], os.path.join(output_folder, f'residuals_{i}'))
            save_fct(rr[i], os.path.join(output_folder, f'scaled_residuals_{i}'))

    def dump(self, path, kwargs, norm, data=None, sigma_2=None, masks=None, save_output_level=4, format='hdf5'):
        """
        Stores information in a given file in pickle or hdf5 format (recommended).

        :param path: Filename of the output.
        :param kwargs: Dictionary containing the fitted value of the model
        :param norm: Normalisation factor of your data. This is an important to save if you want to get the correct photometry.
        :param data: (Nstar x image_size x image_size) array containing the data
        :param sigma_2: (Nstar x image_size x image_size) array containing the noise maps
        :param masks: (Nstar x image_size x image_size) array containing the noise maps
        :param save_output_level: Int. Level of output product to save: 1-just the parameters of the model, 2- add the input data, 3- add the output products (background, narrow PSF, full PSF) 4- add the output products for every image.

        """
        if format == 'pkl':
            with open(path, 'wb') as f:
                pkl.dump([self, kwargs, norm], f, protocol=pkl.HIGHEST_PROTOCOL)
        elif format == 'hdf5':
            kwargs_model = {
                'image_size': int(self.image_size),
                'number_of_sources': int(self.M),
                'upsampling_factor': int(self.upsampling_factor),
                'gaussian_fwhm': int(self.gaussian_size),
                'convolution_method': str(self.convolution_method),
                'gaussian_kernel_size': int(self.gaussian_size),
                'include_moffat': bool(self.include_moffat),
                'elliptical_moffat': bool(self.elliptical_moffat),
            }

            with h5py.File(path, 'w') as f:
                dset = f.create_dataset("kwargs_options", data=json.dumps(kwargs_model))
                dset = f.create_dataset("kwargs_PSF", data=json.dumps(convert_numpy_array_to_list(kwargs)))
                dset = f.create_dataset("Norm", data=norm)

                if save_output_level > 1:
                    if data is not None:
                        dset = f.create_dataset("Data", data=data)
                    if sigma_2 is not None:
                        dset = f.create_dataset("Sigma2", data=sigma_2)
                    if masks is not None:
                        dset = f.create_dataset("Masks", data=masks)

                if save_output_level > 2:
                    narrow = self.get_narrow_psf(**kwargs, norm=True)
                    full = self.get_full_psf(**kwargs, norm=True, high_res=True)
                    background = self.get_background(kwargs['kwargs_background'])
                    analytic = self.get_moffat(kwargs['kwargs_moffat'], norm=True)

                    dset = f.create_dataset("Narrow PSF", data=narrow)
                    dset = f.create_dataset("Full PSF", data=full)
                    dset = f.create_dataset("Background", data=background)
                    dset = f.create_dataset("Analytic", data=analytic)

                if save_output_level > 3:
                    full_psfs = self.model(**kwargs)
                    residuals = data - full_psfs
                    scaled_residuals = jnp.abs(residuals) / jnp.sqrt(sigma_2)
                    dset = f.create_dataset("Full PSF cube", data=full_psfs)
                    dset = f.create_dataset("Residuals cube", data=residuals)
                    dset = f.create_dataset("Scaled residuals cube", data=scaled_residuals)

        else:
            raise NotImplementedError(f'Unrecognized format {format}. Choose between pkl and hdf5.')

    def smart_guess(self, data, fixed_background=True, guess_method='barycenter', masks=None, offset_limit=None, guess_fwhm_pixels=3.):
        """
        Returns an initial guess of the kwargs, given the input data.

        :param data: array of shape (nimage, npix, npix) containing the input data
        :param fixed_background: fixes the background to 0
        :type fixed_background: bool
        :param guess_method: Method to guess the position of the point sources. Choose between 'barycenter' and 'max'
        :type guess_method: str
        :param offset_limit: Upper and lower bounds for the center of the star in "big" pixel. Will be used in the kwargs_down/up['kwargs_gaussian']['x0'], kwargs_down/up['kwargs_gaussian']['y0'].
        :type offset_limit: float
        :param guess_fwhm_pixels: the estimated FWHM of the PSF, is used to initialize the moffat. Default 3.
        :type guess_fwhm_pixels: float

        :return: kwargs containing an initial guess of the parameters
        """

        initial_fwhm = guess_fwhm_pixels
        initial_beta = 2.
        initial_background = jnp.zeros((self.image_size_up ** 2))

        # Positions (initialisation at the center of gravity)
        x0_est = np.zeros(len(data))
        y0_est = np.zeros(len(data))

        # need a grid of pixels for the center of gravity:
        X, Y = jnp.indices(data[0].shape)
        # we'll recenter the positions in the loop:
        # ( -1 because coordinates start at 0)
        centerpos = (self.image_size - 1) / 2.

        if guess_method == 'barycenter':
            # calculate center of gravity for each epoch:
            for i in range(len(data)):
                currentimage = data[i]
                if masks is not None:
                    currentimage *= masks[i]

                # total weight of the image:
                partition = np.nansum(currentimage)
                # first moment: weight coordinates by image values
                x0 = np.nansum(X * currentimage) / partition
                y0 = np.nansum(Y * currentimage) / partition
                # x0 and y0 have their origin at top-left of image.
                x0_est[i] = y0 - centerpos
                y0_est[i] = x0 - centerpos  # x and y needs to be inverted

        elif guess_method == 'max':
            # Positions (initialisation to the brightest pixel)
            x0_est = np.zeros(len(data))
            y0_est = np.zeros(len(data))
            for i in range(len(data)):
                indices = np.where(data[i, :, :] == data[i, :, :].max())
                x0_est[i] = (indices[1] - self.image_size / 2.)
                y0_est[i] = (indices[0] - self.image_size / 2.) #x and y needs to be inverted

        elif guess_method == 'center':
            # Positions (initialisation to the brightest pixel)
            x0_est = np.zeros(len(data))
            y0_est = np.zeros(len(data))
        else :
            raise ValueError('Guess methods unknown. PLease choose between "max", "center" and "barycenter".')

        # Amplitude (use the total flux to scale the amplitude parameters)
        mean_flux = data.sum() / len(data)
        ratio = jnp.array([data[i].sum() / mean_flux for i in range(len(data))])
        initial_a = jnp.ones(len(data)) * ratio
        if self.elliptical_moffat:
            kwargs_moffat_guess = {'fwhm_x': initial_fwhm,'fwhm_y': initial_fwhm, 'phi': 0., 'beta': initial_beta, 'C': 1.}
            kwargs_moffat_up = {'fwhm_x': self.image_size, 'fwhm_y': self.image_size, 'phi': np.pi / 2., 'beta': 50.,
                                'C': jnp.inf}
            kwargs_moffat_down = {'fwhm_x': 2., 'fwhm_y': 2., 'phi': 0., 'beta': 0., 'C': 0.}
        else:
            kwargs_moffat_guess = {'fwhm': initial_fwhm, 'beta': initial_beta, 'C': 1.}
            kwargs_moffat_up = {'fwhm': self.image_size, 'beta': 50., 'C': jnp.inf}
            kwargs_moffat_down = {'fwhm': 2., 'beta': 0., 'C': 0.}

        flux_moffat = Downsample(self.get_moffat(kwargs_moffat_guess, norm=False), factor=self.upsampling_factor).sum()
        initial_C = float(mean_flux / flux_moffat)

        kwargs_moffat_guess['C']=initial_C
        kwargs_init = {
            'kwargs_moffat': kwargs_moffat_guess,
            'kwargs_gaussian': {'a': initial_a * initial_C, 'x0': x0_est, 'y0': y0_est},
            'kwargs_background': {'background': initial_background},
        }

        kwargs_fixed = {
            'kwargs_moffat': {},
            'kwargs_gaussian': {},
            # 'kwargs_background': [{}],
            'kwargs_background': {},
        }
        if fixed_background:
            kwargs_fixed['kwargs_background']['background'] = initial_background

        if offset_limit is None:
            offset_limit = self.image_size / 2.

        # Default value for boundaries
        kwargs_up = {
            'kwargs_moffat': kwargs_moffat_up,
            'kwargs_gaussian': {'a': list([jnp.inf for i in range(len(data))]),
                                'x0': list([offset_limit for i in range(len(data))]),
                                'y0': list([offset_limit for i in range(len(data))])
                                },
            'kwargs_background': {'background': list([jnp.inf for i in range(self.image_size_up ** 2)])},
        }

        kwargs_down = {
            'kwargs_moffat': kwargs_moffat_down,
            'kwargs_gaussian': {'a': list([0 for i in range(len(data))]),
                                'x0': list([-offset_limit for i in range(len(data))]),
                                'y0': list([-offset_limit for i in range(len(data))]),
                                },
            'kwargs_background': {'background': list([-jnp.inf for i in range(self.image_size_up ** 2)])},
        }

        return kwargs_init, kwargs_fixed, kwargs_up, kwargs_down


def load_PSF_model(input_file, format='hdf5'):
    """ Load PSF model class from hdf5 or pickle file"""

    if format == 'pkl':
        with open(input_file, 'rb') as f:
            model, kwargs, norm = pkl.load(f)
            data, sigma_2, masks = None, None, None

    elif format == 'hdf5':
        with h5py.File(input_file, 'r') as f:
            kwargs_model = json.loads(f['kwargs_options'][()])
            model = PSF(**kwargs_model)
            kwargs = json.loads(f['kwargs_PSF'][()])
            kwargs = convert_list_to_numpy_array(kwargs)
            norm = f['Norm'][()]

            if 'Data' in f.keys():
                data = f['Data'][()]
            else:
                print(f'No Data found in {input_file}')
                data = None
            if 'Sigma2' in f.keys():
                sigma_2 = f['Sigma2'][()]
            else:
                print(f'No Noise maps found in {input_file}')
                sigma_2 = None
            if 'Masks' in f.keys():
                masks = f['Masks'][()]
            else:
                print(f'No masks found in {input_file}')
                masks = None
    else:
        raise NotImplementedError(f'Unrecognized format {format}. Choose between pkl and hdf5.')
    return model, kwargs, norm, data, sigma_2, masks
