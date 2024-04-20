import numpy as np


def get_llf_(y, fit):
    # return log likelihood
    nobs = len(y)
    resid = y - fit
    ssr = np.sum((resid)**2)
    llf = - nobs/2 * (np.log(2*np.pi) + np.log(ssr / nobs) + 1)
    return llf


def get_aic(y, fit, n_param):
    llf = get_llf_(y, fit)
    return 2*n_param - 2*llf


def get_bic(y, fit, n_param):
    llf = get_llf_(y, fit)
    return n_param*np.log(len(y)) - 2*llf
