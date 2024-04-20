import numpy as np
import pandas as pd


def bin_column(df, col='', binsize=1, binlabels='center'):
    bins = np.arange(df[col].min(), df[col].max()+2*binsize, binsize)
    if binlabels == 'left':
        labels = bins[:-1]
    elif binlabels == 'right':
        labels = bins[1:]
    else:
        labels = bins[1:]-binsize/2
    df[f'{col}_bin'] = (pd.cut(df[col], bins,
                               labels=labels,
                               include_lowest=True,
                               right=False)
                        .astype({col: 'float64'}))
    return df


def get_histogram(df_in, col: str, binsize=1, binlabels='center', density: bool = False,
                  groupby: str = None, discrete: bool = False):
    if not discrete:
        df_in = (bin_column(df_in, col=col, binsize=binsize, binlabels=binlabels)
                 .drop(columns=col)
                 .rename(columns={f'{col}_bin': col})
                 )
    df_out = (df_in
              .pipe(lambda df: df.groupby(groupby, sort=False) if groupby else df)
              [col]
              .value_counts(normalize=density, sort=False)
              .reset_index()
              )
    return df_out


def order_categories(df, col: str, order: list):
    df = (df.assign(tmp_col=lambda df:
                    df[col]
                    .astype('category')
                    .cat.reorder_categories(order, ordered=True))
            .drop(columns=col)
            .rename(columns={'tmp_col': col})
            .sort_values(by=col)
          )
    return df
