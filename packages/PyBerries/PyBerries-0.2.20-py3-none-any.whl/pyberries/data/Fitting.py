import inspect
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

from ..stats import get_aic, get_bic, get_llf_


class Fit():

    def __init__(self, df_in, x: str, y: str, model=None, model_type: str = None,
                 groupby: str = 'Group', p0=None, param_format: str = 'long'):

        assert model or model_type, 'Must provide either a model_type or a model function'
        assert param_format in ['long', 'wide'], \
            f'param_format "{param_format}" not recognised (must be "long" or "wide")'
        if model:
            self.model = model
            self.model_type = 'custom'
        else:
            self.model_type = model_type
            self.model = get_model(model_type)
        self.model_parameters = inspect.getfullargspec(self.model).args[1:]
        if p0:
            model_args = len(self.model_parameters)
            assert len(p0) == model_args, \
                f'Number of initial parameters ({len(p0)}) does not match number of model arguments ({model_args})'
        fit_parameters = pd.DataFrame(columns=['Group', 'Value', 'Parameter'])
        llf = dict()
        aic = dict()
        bic = dict()
        df_out = pd.DataFrame()
        i = 0
        for name, data in df_in.groupby(groupby, sort=False):
            groupName = '--'.join(map(str, name)) if isinstance(name, tuple) else str(name)
            flag = True
            try:
                popt, _ = curve_fit(self.model, data[x], data[y], p0=p0)
            except Exception as e:
                flag = False
                print(f'Fit for dataset {name} failed: {e}')
            if flag:
                for k, param in enumerate(popt):
                    fit_parameters.loc[i] = {'Group': groupName,
                                             'Value': param,
                                             'Parameter': self.model_parameters[k]
                                             }
                    i += 1
                data = data.assign(Fit=self.model(data[x], *popt),
                                   Residuals=lambda df: data[y] - df.Fit
                                   )
                llf[groupName] = get_llf_(data[y], data['Fit'])
                aic[groupName] = get_aic(data[y], data['Fit'], len(popt))
                bic[groupName] = get_bic(data[y], data['Fit'], len(popt))
                df_out = pd.concat([df_out, data], axis=0, ignore_index=True)
        fit_parameters[groupby] = (fit_parameters['Group'].str.split('--', expand=True))
        if param_format == 'wide':
            fit_parameters = (pd.pivot_table(fit_parameters, values='Value', index=groupby, columns='Parameter')
                              .reset_index()
                              )
        self.data = df_out
        self.llf = llf
        self.aic = aic
        self.bic = bic
        self.parameters = fit_parameters
        self.groupby = groupby

    def __str__(self):
        return f'Fit with parameters: (model={self.model_type}, Groupby={self.groupby})'


def get_model(model_type=''):
    if model_type == 'monoexp_decay':
        def model(x, Amplitude, Rate):
            return Amplitude*np.exp(-Rate*x, dtype='float64')
    elif model_type == 'biexp_decay':
        def model(x, Amplitude_1, Rate_1, Amplitude_2, Rate_2):
            return Amplitude_1*np.exp(-Rate_1*x, dtype='float64') + Amplitude_2*np.exp(-Rate_2*x, dtype='float64')
    elif model_type == 'monoexp_decay_offset':
        def model(x, Amplitude, Rate, offset):
            return Amplitude*np.exp(-Rate*x) + offset
    elif model_type == 'linear':
        def model(x, slope, offset):
            return slope*x+offset
    return model
