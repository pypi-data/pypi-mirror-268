from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def heatmap_metrics(spot_df):
    return (spot_df
            .assign(normLongCoord=lambda df: df.SpineCurvilinearCoord / df.SpineLength - 0.5,
                    normShortCoord=lambda df: df.SpineRadialCoord / df.SpineRadius,
                    centerLongCoord=lambda df: df.SpineCurvilinearCoord - df.SpineLength / 2,
                    )
            )


def tracking_Dapp(df, trim: int = 0, exp_time: float = 1):
    return (df
            .dropna()
            .loc[df.t0_IntervalCount_1 > trim]  # Remove tracks of less than X frames
            .assign(Dapp=(lambda df: df.t4_MSD_1/(trim*exp_time)))
            )


def pca(df, include: list, n_components: int = 2, scaling: bool = True):
    str_columns = df[include].select_dtypes('object').columns
    assert str_columns.empty, f'Cannot run PCA on non-numerical columns: {list(str_columns)}'
    scaler = StandardScaler() if scaling else None
    model = PCA(n_components=n_components)
    pipeline = make_pipeline(scaler, model)
    pca_features = pipeline.fit_transform(df[include])
    return (df.assign(**{f'pca_{k}': pca_features[:, k]
                         for k in range(pca_features.shape[1])})
            )


def weighted_movmean(df, col: str, window: int, weights: str):
    df[f'{col}_movmean'] = (df
                            [col]
                            .mul(df[weights])
                            .rolling(window, min_periods=0, center=True)
                            .sum()
                            .div(df[weights]
                                 .rolling(window, min_periods=0, center=True)
                                 .sum()
                                 )
                            )
    return df
