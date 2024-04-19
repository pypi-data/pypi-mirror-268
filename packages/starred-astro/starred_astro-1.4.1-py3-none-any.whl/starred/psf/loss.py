import warnings

import jax.numpy as jnp
import numpy as np
from starred.utils.jax_utils import decompose, scale_norms


class Loss(object):
    """
    Class that manages the (auto-differentiable) loss function, defined as:
    L = - log(likelihood) - log(regularization)

    Note that gradient, hessian, etc. are computed in the ``InferenceBase`` class.

    """

    def __init__(self, data, psf_class, param_class, sigma_2, N, masks=None,
                 regularization_terms='l1_starlet', regularization_strength_scales=0, regularization_strength_hf=0,
                 regularization_strength_positivity=0, regularize_full_psf=True,
                 W=None):
        """
        :param data: array containing the observations
        :param psf_class: Point Spread Function (PSF) class from ``starred.psf.psf``
        :param param_class: parameters class from ``starred.psf.parameters``
        :param sigma_2: array containing the square of the noise maps
        :param N: number of observations stamps
        :type N: int
        :param masks: array containing the masks for the PSF (if given)
        :param regularization_terms: information about the regularization terms
        :type regularization_terms: str
        :param regularization_strength_scales: Lagrange parameter that weights intermediate scales in the transformed domain.
        :type regularization_strength_scales: float
        :param regularization_strength_hf: Lagrange parameter weighting the highest frequency scale
        :type regularization_strength_hf: float
        :param regularization_strength_positivity: Lagrange parameter weighting the positivity of the full PSF. 0 means no positivity constraint (recommended).
        :type regularization_strength_positivity: float
        :param regularize_full_psf: True if you want to regularize the Moffat and the background (recommended). False regularizes only the background
        :type regularize_full_psf: bool
        :param W: weight matrix. Shape (n_scale, n_pix*subsampling_factor, n_pix*subsampling_factor)

        """
        self._data = data
        self._psf = psf_class
        self._param = param_class
        self.N = N
        self._sigma_2 = sigma_2
        self.W = W
        self.regularize_full_psf = regularize_full_psf
        self._masks = masks

        self._init_likelihood()
        self._init_regularizations(regularization_terms, regularization_strength_scales, regularization_strength_hf,
                                   regularization_strength_positivity)

        self._penalty = 1e10

    def __call__(self, args):
        return self.loss(args)

    def loss(self, args):
        """Defined as the negative log(likelihood*regularization)"""
        kwargs = self._param.args2kwargs(args)
        neg_log = - self._log_likelihood(kwargs)
        if self._st_src_lambda != 0 or self._st_src_lambda_hf != 0:
            neg_log -= self._log_regul(kwargs)
        if self._pos_lambda !=0 :
            neg_log -= self._log_regul_positivity(kwargs)

        return jnp.nan_to_num(neg_log, nan=1e15, posinf=1e15, neginf=1e15)
     
    def update_dataset(self, newdata, newsigma2, newW, newparam_class):
        """Updates the dataset."""
        self._update_data(newdata, newsigma2)
        self._update_parameters(newparam_class)
        if newW is not None:
            self._update_weights(newW)
    
    def _update_parameters(self, param_class):
        """Updates the parameters."""
        self._param = param_class
        
    def _update_data(self, newdata, newsigma2):
        """Updates the data."""
        self._data = newdata
        self._sigma_2 = newsigma2

    def _update_weights(self, W):
        """Updates the weight matrix W."""
        self._st_src_norms = W[:-1]
        self.W = W

    @property
    def data(self):
        """Returns the observations array."""
        return self._data.astype(dtype=np.float32)

    @property
    def sigma_2(self):
        """Returns the noise map array."""
        return self._sigma_2.astype(dtype=np.float32)

    @property
    def masks(self):
        """Returns the masks array."""
        if self._masks is None:
            self._masks = np.ones((self.N, self.data.shape[1], self.data.shape[2]))
        return self._masks.astype(dtype=np.float32)

    def _init_likelihood(self):
        """Intialization of the data fidelity term of the loss function."""
        self._log_likelihood = self._log_likelihood_chi2

    def _init_regularizations(self, regularization_terms, regularization_strength_scales, regularization_strength_hf,
                              regularization_strength_positivity):
        """Intialization of the regularization terms of the loss function."""
        regul_func_list = []
        # add the log-regularization function to the list
        regul_func_list.append(getattr(self, '_log_regul_' + regularization_terms))

        if regularization_terms == 'l1_starlet':
            n_pix_src = min(*self.data[0, :, :].shape) * self._psf.upsampling_factor
            self.n_scales = int(np.log2(n_pix_src))  # maximum allowed number of scales
            if self.W is None:  # old fashion way
                if regularization_strength_scales != 0 and regularization_strength_hf != 0:
                    warnings.warn('lambda is not normalized. Provide the weight map !')
                wavelet_norms = scale_norms(self.n_scales)[:-1]  # ignore coarsest scale
                self._st_src_norms = jnp.expand_dims(wavelet_norms, (1, 2)) * jnp.ones(
                    (n_pix_src, n_pix_src))
            else:
                self._st_src_norms = self.W[:-1]  # ignore the coarsest scale
            self._st_src_lambda = float(regularization_strength_scales)
            self._st_src_lambda_hf = float(regularization_strength_hf)
        else:
            raise NotImplementedError(f'Regularization term {regularization_terms} not implemented yet. Please use "l1_starlet". ')

        # positivity term
        self._pos_lambda = float(regularization_strength_positivity)
        # build the composite function (sum of regularization terms)
        self._log_regul = lambda kw: sum([func(kw) for func in regul_func_list])

    def _log_likelihood_chi2(self, kwargs):
        """Computes the data fidelity term of the loss function using chi2."""
        model_output = self._psf.model(**kwargs)
        diff_squared_weighted = jnp.multiply(self.masks, jnp.subtract(self.data, model_output))**2 / self.sigma_2
        logL = -0.5 * jnp.sum(diff_squared_weighted)
        return logL

    def _log_regul_l1_starlet(self, kwargs):
        """Computes the regularization terms as the sum of:
        the L1 norm of the Starlet transform of the highest frequency scale, and
        the L1 norm of the Starlet transform of all remaining scales (except the coarsest)."""
        if self.regularize_full_psf:
            h = self._psf.get_narrow_psf(**kwargs, norm=False)
        else:
            h = self._psf.get_background(kwargs['kwargs_background'])
        st = decompose(h, self.n_scales)[:-1]  # ignore the coarsest scale, which is a constant
        st_weighted_l1_hf = jnp.sum(self._st_src_norms[0] * jnp.abs(st[0]))  # first scale (i.e. high frequencies)
        st_weighted_l1 = jnp.sum(
            self._st_src_norms[1:] * jnp.abs(st[1:]))  # other scales, we ignore the coarsest scale in W as well
        l1_tot_regul = - (self._st_src_lambda_hf * st_weighted_l1_hf + self._st_src_lambda * st_weighted_l1)
        return (l1_tot_regul / self._psf.upsampling_factor ** 2) * self.N

    def _log_regul_positivity(self, kwargs):
        if self._pos_lambda > 0.:
            #penalise if the full PSF model contains <0 pixels (narrow PSF can have <0 pixels!)
            psf = self._psf.get_full_psf(**kwargs)
            sum_pos = -jnp.where(psf < 0., psf, 0.).sum()
            return - self._pos_lambda * sum_pos * self.N
        else:
            return 0.

    def reduced_chi2(self, kwargs):
        """
        Return the reduced chi2, given some model parameters

        :param kwargs: dictionary containing all keyword arguments
        """
        return -2 * self._log_likelihood_chi2(kwargs) / (self._psf.image_size ** 2) / self.N
