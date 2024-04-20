from os.path import join

import numpy as np
import pandas as pd

import pyberries as pyb

path = './tests/'
ds = 'Test_data'
data = pyb.data.DatasetPool(path=path, dsList=ds)
ref_bacteria = pd.read_csv(join(path, ds, f"{ds}_{0}.csv"), sep=';', low_memory=False)
ref_CFP = pd.read_csv(join(path, ds, f"{ds}_{1}.csv"), sep=';', low_memory=False)


class TestDatasetPool():

    def test_data_import(self):
        assert len(data.Bacteria) == len(ref_bacteria)
        assert len(data.CFP_spots) == len(ref_CFP)

    def test_describe(self):
        data.describe('mean')

    def test_has_na(self):
        data.has_na()

    def test_head(self):
        data.head(2)

    def test_dropna(self):
        data2 = data.dropna()
        assert len(data2.CFP_spots) < len(data.CFP_spots)

    def test_fillna(self):
        data2 = data.fillna(value=0)
        assert data2.CFP_spots.isna().sum().sum() == 0

    def test_set_type(self):
        data2 = data.set_type(object_name='Bacteria', type_dict={'SpineLength': 'float32'})
        assert data2.Bacteria.SpineLength.dtype == 'float32'

    def test_drop_duplicates(self):
        data2 = data.drop_duplicates(object_name='Bacteria', subset='Position')
        assert len(data2.Bacteria) == len(data.Bacteria.Position.unique())

    def test_rename_cols(self):
        data2 = pyb.data.DatasetPool(path=path, dsList=ds, rename_cols={'SpineLength': 'CellLength'})
        assert 'CellLength' in data2.Bacteria.columns
        assert 'SpineLength' not in data2.Bacteria.columns

    def test_filtering(self):
        data2 = pyb.data.DatasetPool(path=path, dsList=ds, filters={'Bacteria': 'SpineLength > 3'})
        assert len(data2.Bacteria) == len(ref_bacteria.query('SpineLength > 3'))
        data3 = data.apply_filters(filters={'Bacteria': 'SpineLength > 3'})
        assert len(data3.Bacteria) == len(ref_bacteria.query('SpineLength > 3'))

    def test_filter_propagation(self):
        data2 = data.apply_filters(filters={'Bacteria': 'SpineLength > 3'})
        assert len(data2.CFP_spots) == 42

    def test_parent_filter(self):
        data2 = data.apply_filters(filters={'CFP_spots': 'DistCC_oc2 < .4'})
        data2.filter_parent(object_name='CFP_spots', inplace=True)
        assert len(data2.Bacteria) == 25
        assert len(data2.CFP_spots) == 25

    def test_add_metadata(self):
        data.add_metadata(['DateTime'], inplace=True)
        assert 'DateTime' in data.Bacteria.columns

    def test_parents(self):
        parents = {'Bacteria': None, 'CFP_spots': 'Bacteria',
                   'mCherry_spots': 'Bacteria', 'YFP_spots': 'Bacteria'}
        assert data._parents == parents

    def test_rename(self):
        data2 = data.rename_object(rename={'Bacteria': 'Bac'})
        assert ('Bac' in data2.objects) and ('Bacteria' not in data2.objects)
        assert (data2._parents['CFP_spots'] == 'Bac') and ('Bacteria' not in data2._parents.keys())
        assert not data2.Bac.empty

    def test_get_idx(self):
        data2 = data.get_idx(object_name='Bacteria', idx=1, indices='Indices', newcol='new_col')
        test_index = (ref_bacteria['Indices']
                      .str.split('-', expand=True)
                      .iloc[:, 1]
                      .astype('int64')
                      )
        assert data2.Bacteria.new_col.equals(test_index)

    def test_get_histogram(self):
        hist = pyb.data.get_histogram(data.Bacteria, col='SpineLength', groupby='Dataset',
                                      discrete=False, binsize=0.5, density=True)
        assert not hist.empty

    def test_bin_column(self):
        data2 = data.bin_column(object_name='Bacteria', col='SpineLength', binsize=1)
        assert 'SpineLength_bin' in data2.Bacteria.columns

    def test_heatmap_metrics(self):
        data2 = data.heatmap_metrics(object_name='CFP_spots')
        assert 'normLongCoord' in data2.CFP_spots.columns

    def test_pca(self):
        data2 = data.pca(object_name='Bacteria', include=['SpineWidth', 'SpineLength', 'CFPCount'])
        assert 'pca_0' in data2.Bacteria.columns
        assert 'pca_1' in data2.Bacteria.columns

    def test_weighted_movmean(self):
        data2 = data.weighted_movmean(object_name='Bacteria', col='SpineLength', window=5, weights='SpineWidth')
        assert 'SpineLength_movmean' in data2.Bacteria.columns

    def test_add_from_parent(self):
        data2 = data.add_from_parent(object_name='CFP_spots', col=['SpineWidth', 'mCherryCount'])
        assert 'SpineWidth' in data2.CFP_spots.columns
        assert 'mCherryCount' in data2.CFP_spots.columns

    def test_add_from_child(self):
        data2 = data.add_from_child(object_name='Bacteria', child='CFP_spots', col='DistCC_oc2',
                                    multiple='min', rename='CFP_mCherry_min_dist')
        assert 'CFP_mCherry_min_dist' in data2.Bacteria.columns

    def test_split_fuse(self):
        data_test = (data
                     .split_column(object_name='Bacteria', col='Indices',
                                   new_cols=['Indices_0', 'Indices_1'], delimiter='-')
                     .fuse_columns(object_name='Bacteria',
                                   columns=['Indices_0', 'Indices_1'], new='Indices_fused', delimiter='-')
                     )
        assert 'Indices_0' in data_test.Bacteria.columns
        assert 'Indices_fused' in data_test.Bacteria.columns

    def test_copy(self):
        data_copy = data.copy()
        data_copy.Bacteria = pd.DataFrame()
        assert len(data.Bacteria) != len(data_copy.Bacteria)


class TestFit():

    def test_Fit(self):
        def model(x, a, b):
            return a*x+b
        test_fit = pyb.data.Fit(data.Bacteria, x='SpineWidth', y='SpineLength', model=model)
        assert not test_fit.data.empty
        models = ['monoexp_decay', 'biexp_decay', 'monoexp_decay_offset', 'linear']
        model = pyb.data.get_model('monoexp_decay')
        data.Bacteria = (data.Bacteria
                         .assign(x=np.linspace(0, len(data.Bacteria), len(data.Bacteria)),
                                 y=lambda df: model(df.x, Amplitude=10, Rate=0.1)
                                 )
                         )
        for mod in models:
            test_fit = pyb.data.Fit(data.Bacteria, x='x', y='y', model_type=mod)
            assert not test_fit.parameters.empty


class TestStats():

    def test_ttest_1way(self):
        res = pyb.stats.ttest_1way(data=data.Bacteria, col='SpineLength', test_mean=2)
        assert round(res.statistic) == 9

    def test_ttest_2way(self):
        res = pyb.stats.ttest_2way(data=data.Bacteria, col='SpineLength', by='CFPCount')
        assert round(res.statistic) == -5

    def test_tukey(self):
        res = pyb.stats.tukey_test(data=data.Bacteria, col='SpineLength', by='CFPCount')
        assert len(res.pvalue) == 2

    def test_kstest(self):
        res = pyb.stats.ks_test(data=data.Bacteria, col='SpineLength', by='CFPCount')
        assert round(res.statistic_location) == 3
