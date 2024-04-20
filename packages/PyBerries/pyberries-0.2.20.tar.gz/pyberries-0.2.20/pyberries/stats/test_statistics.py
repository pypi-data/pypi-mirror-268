from scipy.stats import ttest_ind, ttest_1samp, tukey_hsd, levene, ks_2samp


def ttest_2way(data, col: str, by: list, levene_threshold=0.05):
    if isinstance(by, list):
        data = (data
                .assign(Groupby=lambda df: df[by].astype('str').agg(' '.join, axis=1))
                )
        by = 'Groupby'
    categories = data[by].unique()
    assert len(categories) == 2, 'Cannot perform 2way t-test on more than 2 groups'
    group1 = data[data[by] == categories[0]][col]
    group2 = data[data[by] == categories[1]][col]
    equal_var = levene(group1, group2).pvalue < levene_threshold
    res = ttest_ind(group1, group2, equal_var=equal_var)
    print(f'Effect size: {abs(group1.mean()-group2.mean())/data[col].std()}')
    return res


def ttest_1way(data, col: str, test_mean: float):
    res = ttest_1samp(data[col], test_mean)
    print(f'Effect size: {abs(data[col].mean()-test_mean)/data[col].std()}')
    return res


def tukey_test(data, col: str, by: list):
    if isinstance(by, list):
        data = (data
                .assign(Groupby=lambda df: df[by].astype('str').agg(' '.join, axis=1))
                )
        by = 'Groupby'
    categories = data[by].unique()
    print(f'Groups: {categories}')
    test_data = [data[data[by] == cat][col].tolist() for cat in categories]
    res = tukey_hsd(*test_data)
    return res


def ks_test(data, col: str, by: str):
    if isinstance(by, list):
        data = (data
                .assign(Groupby=lambda df: df[by].astype('str').agg(' '.join, axis=1))
                )
        by = 'Groupby'
    categories = data[by].unique()
    assert len(categories) == 2, 'Cannot perform Kolmogorov-Smirnoff test on more than 2 groups'
    res = ks_2samp(data[data[by] == categories[0]][col], data[data[by] == categories[1]][col])
    return res
