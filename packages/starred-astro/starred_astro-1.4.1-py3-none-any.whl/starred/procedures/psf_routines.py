import numpy as np
from copy import deepcopy
import warnings

from starred.psf.psf import PSF
from starred.psf.loss import Loss
from starred.optim.optimization import Optimizer
from starred.psf.parameters import ParametersPSF
from starred.utils.noise_utils import propagate_noise


def build_psf(image, noisemap, subsampling_factor,
              masks=None, n_iter_analytic=40, n_iter_adabelief=2000,
              guess_method_star_position='barycenter',
              guess_fwhm_pixels=3.):
    """
    
    Routine taking in cutouts of stars (shape (N, nx, ny), with N the number of star cutouts, and nx,ny the shape of each cutout)
    and their noisemaps (same shape), producing a narrow PSF with pixel grid of the given subsampling_factor

    Parameters
    ----------
    image : array, shape (imageno, nx, ny)
        array containing the data
    noisemap : array, shape (imageno, nx, ny)
        array containing the noisemaps.
    subsampling_factor : int
        by how much we supersample the PSF pixel grid compare to data..
    masks: optional, array of same shape as image and noisemap containing 1 for pixels to be used, 0 for pixels to be ignored.
    n_iter_analytic: int, optional, number of iterations for fitting the moffat in the first step
    n_iter_adabelief: int, optional, number of iterations for fitting the background in the second step
    guess_method_star_position: str, optional, one of 'barycenter', 'max' or 'center'
    guess_fwhm_pixels: float, the estimated FWHM of the PSF, is used to initialize the moffat. Default 3.

    Returns
    -------
    result : dictionary
        dictionary containing the narrow PSF (key narrow_psf) and other useful things.

    """
    
    # normalize by max of data(numerical precision best with scale ~ 1)
    norm = np.nanmax(image)
    image /= norm
    noisemap /= norm

    model = PSF(image_size=image[0].shape[0], number_of_sources=len(image), 
                upsampling_factor=subsampling_factor, 
                convolution_method='fft',
                include_moffat=True,
                elliptical_moffat=True)

    smartguess = lambda im: model.smart_guess(im, fixed_background=True, guess_method=guess_method_star_position,
                                              guess_fwhm_pixels=guess_fwhm_pixels)

    # Parameter initialization.
    kwargs_init, kwargs_fixed, kwargs_up, kwargs_down = smartguess(image)

    # smartguess doesn't know about cosmics, other stars ...
    # so we'll be a bit careful.
    medx0 = np.median(kwargs_init['kwargs_gaussian']['x0'])
    medy0 = np.median(kwargs_init['kwargs_gaussian']['y0'])
    kwargs_init['kwargs_gaussian']['x0'] = medx0 * np.ones_like(kwargs_init['kwargs_gaussian']['x0'])
    kwargs_init['kwargs_gaussian']['y0'] = medy0 * np.ones_like(kwargs_init['kwargs_gaussian']['y0'])

    parameters = ParametersPSF(kwargs_init, 
                               kwargs_fixed, 
                               kwargs_up=kwargs_up, 
                               kwargs_down=kwargs_down)

    loss = Loss(image, model, parameters, noisemap**2, len(image),
                regularization_terms='l1_starlet', 
                regularization_strength_scales=0, 
                regularization_strength_hf=0,
                masks=masks)

    optim = Optimizer(loss, 
                      parameters, 
                      method='l-bfgs-b')

    # fit the moffat:
    best_fit, logL_best_fit, extra_fields, runtime = optim.minimize(maxiter=n_iter_analytic,
                                                                    restart_from_init=True)

    kwargs_partial = parameters.args2kwargs(best_fit)

    # now moving on to the background.
    # Release backgound, fix the moffat
    kwargs_fixed = {
        'kwargs_moffat': {'fwhm_x': kwargs_partial['kwargs_moffat']['fwhm_x'], 
                          'fwhm_y': kwargs_partial['kwargs_moffat']['fwhm_y'],
                          'phi': kwargs_partial['kwargs_moffat']['phi'],
                          'beta': kwargs_partial['kwargs_moffat']['beta'], 
                          'C': kwargs_partial['kwargs_moffat']['C']},
        'kwargs_gaussian': {},
        'kwargs_background': {},
    }

    parametersfull = ParametersPSF(kwargs_partial,
                                   kwargs_fixed, 
                                   kwargs_up, 
                                   kwargs_down)

    topass = np.nanmedian(noisemap, axis=0)
    topass = np.expand_dims(topass, (0,))
    W = propagate_noise(model, topass, kwargs_init, 
                        wavelet_type_list=['starlet'], 
                        method='MC', num_samples=100,
                        seed=1, likelihood_type='chi2', 
                        verbose=False, 
                        upsampling_factor=subsampling_factor)[0]
    
    lossfull = Loss(image, model, parametersfull, 
                    noisemap**2, len(image), 
                    regularization_terms='l1_starlet',
                    regularization_strength_scales=1.,
                    regularization_strength_hf=1.,
                    regularization_strength_positivity=0, 
                    W=W, 
                    regularize_full_psf=False,
                    masks=masks)
    

    optimfull = Optimizer(lossfull, parametersfull, method='adabelief')
    
        
    optimiser_optax_option = {
                                'max_iterations':n_iter_adabelief, 'min_iterations':None,
                                'init_learning_rate': 1e-4, 'schedule_learning_rate':True,
                                # important: restart_from_init True
                                'restart_from_init':True, 'stop_at_loss_increase':False,
                                'progress_bar':True, 'return_param_history':True
                              }           
    
    best_fit, logL_best_fit, extra_fields2, runtime = optimfull.minimize(**optimiser_optax_option)
    
    kwargs_final = parametersfull.args2kwargs(best_fit)
    
    ###########################################################################
    # book keeping
    narrowpsf = model.get_narrow_psf(**kwargs_final, norm=True)
    fullpsf   = model.get_full_psf(**kwargs_final, norm=True)
    numpsf    = model.get_background(kwargs_final['kwargs_background'])
    moffat    = model.get_moffat(kwargs_final['kwargs_moffat'], norm=True)
    fullmodel = model.model(**kwargs_final)
    residuals = image - fullmodel
    # approximate chi2: hard to count params with regularization, will be under 1 for good fit -- but indicative.
    chi2      = np.sum(residuals**2 / noisemap**2) / residuals.size

    result = {
        'model_instance': model,
        'kwargs_psf': kwargs_final,
        'narrow_psf': narrowpsf,
        'full_psf': fullpsf,
        'numerical_psf': numpsf,
        'moffat': moffat,
        'models': fullmodel,
        'residuals': residuals,
        'analytical_optimizer_extra_fields': extra_fields,
        'adabelief_extra_fields': extra_fields2,
        'chi2': chi2
    }
    ###########################################################################
    return result


def run_multi_steps_PSF_reconstruction(data, model, parameters, sigma_2, masks=None,
                                       lambda_scales=1., lambda_hf=1., lambda_positivity=0.,
                                       fitting_sequence=[['background'], ['moffat']],
                                       optim_list=['l-bfgs-b', 'adabelief'],
                                       kwargs_optim_list=None,
                                       method_noise='MC', regularize_full_psf=False,
                                       verbose=True):
    """
    A high level function for a custom fitting sequence. Similar to build_psf() but with more options.

    :param data: array containing the observations
    :param model: Point Spread Function (PSF) class from ``starred.psf.psf``
    :param parameters: parameters class from ``starred.psf.parameters``
    :param sigma_2: array containing the square of the noise maps
    :param lambda_scales: Lagrange parameter that weights intermediate scales in the transformed domain.
    :param lambda_hf: Lagrange parameter weighting the highest frequency scale
    :param lambda_positivity: Lagrange parameter weighting the positivity of the full PSF. 0 means no positivity constraint (recommended).
    :param fitting_sequence: list, List of lists, containing the element of the model to keep fixed. Example : [['pts-source-astrometry','pts-source-photometry','background'],['pts-source-astrometry','pts-source-photometry'], ...]
    :param optim_list: List of optimiser. Recommended if background is kept constant : 'l-bfgs-b', 'adabelief' otherwise.
    :param kwargs_optim_list: List of dictionary, containing the setting for the different optimiser.
    :param method_noise: method for noise propagation. Choose 'MC' for an empirical propagation of the noise or 'SLIT' for analytical propagation.
    :param regularize_full_psf: True if you want to regularize the Moffat and the background (recommended). False regularizes only the background
    :param masks: array containing the masks for the PSF (if given)

    :return model, parameters, loss, kwargs_partial_list, LogL_list, loss_history_list
    """

    # Check the sequence
    assert len(fitting_sequence) == len(optim_list), "Fitting sequence and optimiser list have different lenght !"
    if kwargs_optim_list is not None:
        assert len(fitting_sequence) == len(
            kwargs_optim_list), "Fitting sequence and kwargs optimiser list have different lenght !"
    else:
        warnings.warn('No optimiser kwargs provided. Default configuration is used.')
        kwargs_optim_list = [{} for _ in range(len(fitting_sequence))]
    kwargs_init, kwargs_fixed_default, kwargs_up, kwargs_down = deepcopy(parameters._kwargs_init), deepcopy(
        parameters._kwargs_fixed), \
        deepcopy(parameters._kwargs_up), deepcopy(parameters._kwargs_down)

    kwargs_partial_list = [kwargs_init]
    loss_history_list = []
    LogL_list = []
    W = None

    for i, steps in enumerate(fitting_sequence):
        kwargs_fixed = deepcopy(kwargs_fixed_default)
        background_free = True
        print(f'### Step {i + 1}, fixing : {steps} ###')
        for fixed_feature in steps:
            if fixed_feature == 'pts-source-astrometry':
                kwargs_fixed['kwargs_gaussian']['x0'] = kwargs_partial_list[i]['kwargs_gaussian']['x0']
                kwargs_fixed['kwargs_gaussian']['y0'] = kwargs_partial_list[i]['kwargs_gaussian']['y0']
            elif fixed_feature == 'pts-source-photometry':
                kwargs_fixed['kwargs_gaussian']['a'] = kwargs_partial_list[i]['kwargs_gaussian']['a']
                kwargs_fixed['kwargs_moffat']['C'] = kwargs_partial_list[i]['kwargs_moffat']['C']
            elif fixed_feature == 'background':
                # TODO: check if there is a speed up when skipping regularization in the case of a fixed background
                kwargs_fixed['kwargs_background']['background'] = kwargs_partial_list[i]['kwargs_background'][
                    'background']
                background_free = False
            elif fixed_feature == 'moffat':
                if model.elliptical_moffat:
                    kwargs_fixed['kwargs_moffat']['fwhm_x'] = kwargs_partial_list[i]['kwargs_moffat']['fwhm_x']
                    kwargs_fixed['kwargs_moffat']['fwhm_y'] = kwargs_partial_list[i]['kwargs_moffat']['fwhm_y']
                    kwargs_fixed['kwargs_moffat']['phi'] = kwargs_partial_list[i]['kwargs_moffat']['phi']
                else:
                    kwargs_fixed['kwargs_moffat']['fwhm'] = kwargs_partial_list[i]['kwargs_moffat']['fwhm']
                kwargs_fixed['kwargs_moffat']['beta'] = kwargs_partial_list[i]['kwargs_moffat']['beta']
                kwargs_fixed['kwargs_moffat']['C'] = kwargs_partial_list[i]['kwargs_moffat']['C']
            else:
                raise ValueError(
                    f'Steps {steps} is not defined. Choose between "pts-source-astrometry", "pts-source-photometry", "background" or "moffat"')

        # Lift degeneracy between background and Moffat by fixing Moffat amplitude
        if background_free:
            kwargs_fixed['kwargs_moffat']['C'] = kwargs_partial_list[i]['kwargs_moffat']['C']
            lambda_scales_eff = deepcopy(lambda_scales)
            lambda_hf_eff = deepcopy(lambda_hf)
        else:
            # remove regularization for speed up
            lambda_scales_eff = 0.
            lambda_hf_eff = 0.

        # recompile the parameter class as we have changed the number of free parameters
        parameters = ParametersPSF(kwargs_partial_list[i], kwargs_fixed, kwargs_up, kwargs_down)
        loss = Loss(data, model, parameters, sigma_2, model.M, masks=masks, regularization_terms='l1_starlet',
                    regularization_strength_scales=lambda_scales_eff, regularization_strength_hf=lambda_hf_eff,
                    regularization_strength_positivity=lambda_positivity, W=W,
                    regularize_full_psf=regularize_full_psf)

        optim = Optimizer(loss, parameters, method=optim_list[i])
        best_fit, logL_best_fit, extra_fields, runtime = optim.minimize(**kwargs_optim_list[i])
        if verbose:
            try:
                # this will work only for the Jaxopt optimiser, which have a success argument
                if extra_fields['stat'].success:
                    print(
                        f'Success of the step {i + 1} fit in {extra_fields["stat"].iter_num} iterations ({runtime} s)')
                else:
                    print(f'Warning: step {i + 1} fit did not converge !')
            except:
                pass

        # Saving partial results
        kwargs_partial_steps = deepcopy(parameters.best_fit_values(as_kwargs=True))
        loss_history_list.append(extra_fields['loss_history'])
        LogL_list.append(logL_best_fit)

        # compute noise propagation
        W = propagate_noise(model, np.sqrt(sigma_2), kwargs_partial_steps, wavelet_type_list=['starlet'],
                            method=method_noise,
                            num_samples=400, seed=1, likelihood_type='chi2', verbose=False,
                            upsampling_factor=model.upsampling_factor)[0]

        # update kwargs_partial_list
        kwargs_partial_list.append(deepcopy(kwargs_partial_steps))
        if verbose:
            print('Step %i/%i took %2.f seconds' % (i + 1, len(fitting_sequence), runtime))
            print('Kwargs partial at step %i/%i' % (i + 1, len(fitting_sequence)), kwargs_partial_steps)
            print('LogL : ', logL_best_fit)
            print('Overall Reduced Chi2 : ', loss.reduced_chi2(kwargs_partial_steps))

    return model, parameters, loss, kwargs_partial_list, LogL_list, loss_history_list
