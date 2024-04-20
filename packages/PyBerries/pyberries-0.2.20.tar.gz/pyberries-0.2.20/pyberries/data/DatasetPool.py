import copy
from functools import wraps
from os import listdir
from os.path import exists, join
from warnings import warn

import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
from pybacmman.selections import store_selection

import pyberries as pyb

from .util import arg_to_list, dict_val_to_list, read_config, read_metadata


def multiTable(object_name=None, inplace=False, print_obj=False):
    def decorate(func):
        @wraps(func)
        def wrapper(self, *args, object_name=object_name, inplace=inplace, **kwargs):
            dp = self if inplace else self.copy()
            if object_name:
                objects = arg_to_list(object_name)
            else:
                objects = dp.objects
            for obj in objects:
                if not dp[obj].empty:
                    if print_obj:
                        print(obj)
                        func(dp[obj], *args, **kwargs)
                    else:
                        dp[obj] = func(dp[obj], *args, **kwargs)
            if not inplace:
                return dp
        return wrapper
    return decorate


class DatasetPool():

    def __init__(self,
                 path,
                 dsList,
                 groups=[],
                 metadata=[],
                 filters={},
                 rename_cols={},
                 rename_objects={}
                 ):

        self.path = arg_to_list(path)
        self.dsList = arg_to_list(dsList)
        self.groups = groups if groups else list(range(len(dsList)))
        self.objects = []
        self.positions = dict()
        self.object_index = dict()
        self.channelImage = dict()
        self._parents = dict()
        self.rename_cols = rename_cols
        self.rename_objects = rename_objects

        assert (len(self.groups) >= len(self.dsList)), \
            'If groups are provided, one group should be defined per dataset'

        for i, ds in enumerate(self.dsList):
            ds_path = self.path[0] if len(self.path) == 1 else self.path[i]
            assert exists(ds_path), f'Bacmman folder not found: {ds_path}'
            assert exists(join(ds_path, ds)), \
                f'Dataset {ds} not found.\n\
                    Maybe looking for {" or ".join([x for x in listdir(ds_path) if x.startswith(ds[0:6])])}?'
            self.load_dataset(ds_path, ds, self.groups[i], inplace=True)
        self.add_metadata(metadata, inplace=True)
        self.apply_filters(filters, inplace=True)

    def __getitem__(self, name):
        return getattr(self, name)

    def __setitem__(self, name, value):
        return setattr(self, name, value)

    def __str__(self):
        return f'DatasetPool containing objects {self.objects}'

    def load_dataset(self, ds_path, ds, grp, inplace=False):
        dp = self if inplace else self.copy()
        config = read_config(ds_path, ds)
        # Add Viewfield object if measurement table is available
        if exists(join(ds_path, ds, f"{ds}_{-1}.csv")):
            config['object_class_names'].insert(0, 'Viewfield')
            config['object_parents'].insert(0, [])
            start_table = -1
        else:
            start_table = 0
        # Rename objects if specified
        if self.rename_objects:
            for i, obj in enumerate(config['object_class_names']):
                if obj in self.rename_objects.keys():
                    config['object_class_names'][i] = self.rename_objects[obj]
        # Load data tables
        k = 0
        for j, obj in enumerate(config['object_class_names'], start_table):
            dp.object_index[obj] = j
            df_in = (pd.read_csv(join(ds_path, ds, f"{ds}_{j}.csv"), sep=';', low_memory=False)
                     .assign(Dataset=ds,
                             Group=grp)
                     .rename(columns=self.rename_cols)
                     )
            dp[obj] = df_in if obj not in dp.__dict__.keys() else pd.concat([dp[obj], df_in], ignore_index=True, axis=0)
            if config['object_parents'][k]:
                dp._parents[obj] = config['object_class_names'][config['object_parents'][k][0]-start_table]
            else:
                dp._parents[obj] = 'Viewfield' if start_table == -1 else None
            dp.channelImage[obj] = config['channelImage'][k]
            k += 1
        for dup in config['dupChannels']:
            dp.channelImage[dup['name']] = dup['source'][0]
        dp.positions[ds] = config['positions']
        [self.objects.append(obj) for obj in config['object_class_names'] if obj not in self.objects]
        print(f"Dataset {ds}: loaded objects {config['object_class_names']}")
        if not inplace:
            return dp

    def copy(self):
        new_dp = copy.deepcopy(self)
        return new_dp

    @multiTable(inplace=True, print_obj=True)
    def describe(df, agg: str = 'mean', include: str = 'all'):
        include = arg_to_list(include)
        if include != ['all']:
            df = df.filter(items=include + ['Dataset', 'Group'])
            if not [item for item in list(df.columns) + ['All'] if item in include]:
                df = pd.DataFrame()
        df1 = (df
               .groupby('Dataset', sort=False)
               .agg(nObjects=('Dataset', 'count'))
               )
        df2 = (df
               .loc[:, (~df.columns
                        .isin(['Position', 'PositionIdx', 'Indices', 'Frame', 'Idx', 'Time', 'Group']))]
               .groupby('Dataset', sort=False)
               .agg(agg, numeric_only=True)
               )
        if isinstance(agg, list):
            df2.columns = df2.columns.map(' ('.join) + ')'
        df3 = df[['Group', 'Dataset']].drop_duplicates().set_index('Dataset')
        df_out = df3.join([df1, df2])
        display(df_out)

    @multiTable(inplace=True, print_obj=True)
    def has_na(df):
        df = (df
              .loc[:, (~df.columns
                       .isin(['Position', 'PositionIdx', 'Indices', 'Frame', 'Idx', 'Time', 'Group', 'Dataset']))]
              )
        if not df.empty:
            display(df.isna().sum())

    @multiTable()
    def dropna(df, **kwargs):
        return df.dropna(**kwargs)

    @multiTable()
    def fillna(df, col=None, **kwargs):
        if col:
            for c in arg_to_list(col):
                df[c] = df[c].fillna(**kwargs)
        else:
            df = df.fillna(**kwargs)
        return df

    @multiTable()
    def set_type(df, type_dict):
        object_name_type = {key: value for key, value in type_dict.items() if key in df.columns}
        return df.astype(object_name_type)

    @multiTable()
    def drop_duplicates(df, **kwargs):
        return df.drop_duplicates(**kwargs)

    @multiTable(inplace=True, print_obj=True)
    def head(df, nlines: int = 5):
        display(df.head(nlines))

    def add_metadata(self, keys, inplace=False):
        dp = self if inplace else self.copy()
        keys = arg_to_list(keys)
        keys = keys + ['Dataset', 'Position']
        metadata = dict()
        for i, ds in enumerate(dp.dsList):
            ds_path = dp.path[0] if len(dp.path) == 1 else dp.path[i]
            for pos in dp.positions[ds]:
                meta_file = join(ds_path, ds, 'SourceImageMetadata', f'{pos}.json')
                assert exists(meta_file), f'Metadata file "{meta_file}" not found'
                pos_metadata = read_metadata(ds_path, ds, pos)
                for ch, df in pos_metadata.items():
                    if ch in metadata.keys():
                        metadata[ch] = pd.concat([metadata[ch], pos_metadata[ch]], ignore_index=True, axis=0)
                    else:
                        metadata[ch] = pos_metadata[ch]
        for obj, channel in dp.channelImage.items():
            df = dp[obj]
            if not df.empty:
                if metadata[f'channel_{channel}']['Frame'].max() == 0:
                    df = (df
                          .merge(metadata[f'channel_{channel}'][keys],
                                 on=['Dataset', 'Position'],
                                 how='left'
                                 )
                          )
                else:
                    df = (dp[obj]
                          .merge(metadata[f'channel_{channel}'][keys + ['Frame']],
                                 on=['Dataset', 'Position', 'Frame'],
                                 how='left'
                                 )
                          )
                if 'DateTime' in df.columns:
                    df = (df
                          .assign(DateTime=lambda df:
                                  pd.to_datetime(df.DateTime,
                                                 format='%Y%m%d %H:%M:%S.%f'),
                                  TimeDelta=lambda df:
                                  df[['Dataset', 'DateTime']]
                                  .groupby('Dataset')
                                  .transform(lambda x: x - x.iloc[0]),
                                  Time_min=lambda df:
                                  df.TimeDelta.dt.total_seconds().div(60)
                                  )
                          )
                dp[obj] = df
        if not inplace:
            return dp

    def apply_filters(self, filters, inplace=False):
        dp = self if inplace else self.copy()
        filters = dict_val_to_list(filters)
        for target, filter in filters.items():
            if target.lower() == 'all':
                objects = self.objects
            else:
                objects = [target]
            for obj in objects:
                if len(filter) == 1:
                    dp[obj] = dp[obj].query(filter[0])
                elif len(filter) > 1:
                    assert len(filter) == len(dp.dsList), \
                        'If multiple filters are provided, there should be one per dataset'
                    df = pd.DataFrame()
                    i = 0
                    for _, data in dp[obj].groupby('Dataset', sort=False):
                        if filter[i]:
                            df = pd.concat([df, data.query(filter[i])], axis=0)
                        else:
                            df = pd.concat([df, data], axis=0)
                        i += 1
                    dp[obj] = df
        for child, parent in dp._parents.items():
            if parent:
                dp.propagate_filters(parent, child, inplace=True)
        if not inplace:
            return dp

    def propagate_filters(self, parent: str, child: str, inplace=False):
        dp = self if inplace else self.copy()
        if not dp[child].empty:
            dp.get_parent_indices(object_name=child, inplace=True)
            dp[child] = (dp[child]
                         .merge(dp[parent][['Dataset', 'PositionIdx', 'Indices']].drop_duplicates(),
                                suffixes=(None, '_tmp'),
                                left_on=['Dataset', 'PositionIdx', 'ParentIndices'],
                                right_on=['Dataset', 'PositionIdx', 'Indices'])
                         .transform(lambda df: df.loc[:, ~df.columns.str.contains('_tmp')])
                         )
        if not inplace:
            return dp

    def filter_parent(self, object_name, inplace=False):
        dp = self if inplace else self.copy()
        for obj in arg_to_list(object_name):
            parent = self._parents[obj]
            dp.get_parent_indices(object_name=obj, inplace=True)
            dp[parent] = (dp[parent]
                          .merge(dp[obj][['Dataset', 'PositionIdx', 'ParentIndices']]
                                 .drop_duplicates(),
                                 how='inner',
                                 suffixes=(None, '_tmp'),
                                 left_on=['Dataset', 'PositionIdx', 'Indices'],
                                 right_on=['Dataset', 'PositionIdx', 'ParentIndices'])
                          .transform(lambda df: df.loc[:, ~df.columns.str.contains('_tmp')])
                          )
            for child, parent in dp._parents.items():
                if parent:
                    dp.propagate_filters(parent, child, inplace=True)
        if not inplace:
            return dp

    def rename_object(self, rename: dict, inplace=False):
        dp = self if inplace else self.copy()
        for old_name, new_name in rename.items():
            if new_name in dp.objects:
                dp[new_name] = (pd.concat([dp[new_name], dp[old_name]], axis=0)
                                  .reset_index(drop=True, inplace=True))
            else:
                dp[new_name] = dp[old_name]
                dp._parents[new_name] = dp._parents[old_name]
            for child, parent in dp._parents.items():
                if parent == old_name:
                    dp._parents[child] = new_name
            delattr(dp, old_name)
            del dp._parents[old_name]
            dp.objects = list(dp._parents.keys())
        if not inplace:
            return dp

    @multiTable()
    def get_parent_indices(df, indices: str = 'Indices', newcol: str = 'ParentIndices'):
        df[newcol] = (df[indices]
                      .str.split('-', expand=True)
                      .iloc[:, :-1]
                      .agg('-'.join, axis=1)
                      )
        return df

    @multiTable()
    def get_idx(df, idx: int = 0, indices: str = 'Indices', newcol: str = 'ParentIdx'):
        df[newcol] = (df[indices]
                      .str.split('-', expand=True)
                      .iloc[:, idx]
                      .astype('int64')
                      )
        return df

    @multiTable()
    def fuse_columns(df, columns: list = [], new: str = 'new_col', delimiter: str = '-'):
        df[new] = (df[columns]
                   .astype('str')
                   .agg(delimiter.join, axis=1)
                   )
        return df

    @multiTable()
    def split_column(df, col: str, new_cols: list, delimiter: str):
        df[new_cols] = (df[col]
                        .str.split(delimiter, expand=True)
                        )
        return df

    def add_from_parent(self, object_name: str, col: list = [], inplace=False):
        dp = self if inplace else self.copy()
        parent = dp._parents[object_name]
        dp.get_parent_indices(object_name=object_name, inplace=True)
        for c in arg_to_list(col):
            dp[object_name] = (dp[object_name]
                               .merge(dp[parent][['Dataset', 'PositionIdx', 'Indices', c]],
                                      suffixes=(None, '_tmp'),
                                      left_on=['Dataset', 'PositionIdx', 'ParentIndices'],
                                      right_on=['Dataset', 'PositionIdx', 'Indices'])
                               .transform(lambda df: df.loc[:, ~df.columns.str.contains('_tmp')])
                               )
        if not inplace:
            return dp

    def add_from_child(self, object_name: str, child: str, col: list = [], multiple: str = 'mean',
                       rename: list = [], inplace=False):
        dp = self if inplace else self.copy()
        dp.get_parent_indices(object_name=child, inplace=True)
        col = arg_to_list(col)
        rename = arg_to_list(rename) if rename else col
        for c, new_name in zip(col, rename):
            dp[object_name] = (dp[object_name]
                               .merge(dp[child][['Dataset', 'PositionIdx', 'ParentIndices', c]]
                                      .groupby(by=['Dataset', 'ParentIndices'])
                                      .agg(multiple)
                                      .rename(columns={c: new_name}),
                                      how='left',
                                      suffixes=(None, '_tmp'),
                                      left_on=['Dataset', 'PositionIdx', 'Indices'],
                                      right_on=['Dataset', 'PositionIdx', 'ParentIndices'])
                               .transform(lambda df: df.loc[:, ~df.columns.str.contains('_tmp')])
                               )
        if not inplace:
            return dp

    @multiTable()
    def assign(df, **kwargs):
        return df.assign(**kwargs)

    @multiTable()
    def bin_column(df, col: str, binsize=1, binlabels='center'):
        return pyb.data.bin_column(df, col, binsize, binlabels)

    # Pre-defined metrics

    @multiTable()
    def heatmap_metrics(df):
        return pyb.metrics.heatmap_metrics(df)

    @multiTable()
    def tracking_Dapp(df, trim: int = 4, exp_time: float = 0.012):
        return pyb.metrics.tracking_Dapp(df, trim, exp_time)

    @multiTable()
    def pca(df, include: list, n_components: int = 2, scaling: bool = True):
        return pyb.metrics.pca(df, include, n_components, scaling)

    @multiTable()
    def weighted_movmean(df, col: str, window: int, weights: str):
        return pyb.metrics.weighted_movmean(df, col, window, weights)

    # Selection tools

    def add_selection(self, selection_name: str = None, inplace=False):
        dp = self if inplace else self.copy()
        for i, ds in enumerate(self.dsList):
            ds_path = self.path[0] if len(self.path) == 1 else self.path[i]
            if exists(join(ds_path, ds, f"{ds}_Selections.csv")):
                selections = (pd.read_csv(join(ds_path, ds, f"{ds}_Selections.csv"), sep=';', low_memory=False)
                              .assign(Dataset=ds,
                                      dummies=lambda df: df.SelectionName)
                              .pipe(pd.get_dummies, columns=['dummies'], prefix='', prefix_sep='')
                              )
                selection_name = arg_to_list(selection_name) if selection_name else selections.SelectionName.unique()
                for sel_name in selection_name:
                    sel = selections.query(f'SelectionName == "{sel_name}"')
                    object_name = self.objects[sel.ObjectClassIdx.iloc[0]]
                    dp[object_name] = (dp[object_name]
                                       .merge(sel[['Dataset', 'Position', 'Indices', sel_name]],
                                              how='left',
                                              suffixes=(None, '_tmp'),
                                              on=['Dataset', 'Position', 'Indices'])
                                       .transform(lambda df: df.loc[:, ~df.columns.str.contains('_tmp')])
                                       )
            else:
                print(f'Selections file not found for dataset {ds}')
        if not inplace:
            return dp

    def save_selection(self, object_name: str, datasets=None, name: str = None):
        datasets = arg_to_list(datasets) if datasets else self.dsList
        for ds in datasets:
            store_selection(self[object_name].query('Dataset == @ds'), dsName=ds,
                            objectClassIdx=self.object_index[object_name],
                            selectionName=name,
                            port=25333, python_proxy_port=25334, address='127.0.0.1'
                            )

    # Pre-defined plots

    def plot_preset(self, preset: str, object_name: str = '', return_axes: bool = False, **kwargs):
        dp = self.copy()
        hue = kwargs.get('hue', '')
        if isinstance(hue, list):
            dp.fuse_columns(object_name=object_name, cols=hue, new='_'.join(hue), inplace=True)
            kwargs['hue'] = '_'.join(hue)
        if object_name:
            df_in = dp[object_name]
        _, ax = plt.subplots(dpi=130)
        if preset == 'histogram':
            ax = pyb.plots.plot_histogram(df_in, ax=ax, **kwargs)
        elif preset == 'histogram_fit':
            ax = pyb.plots.plot_histogram_fit(df_in, ax=ax, **kwargs)
        elif preset == 'bar':
            ax = pyb.plots.barplot(df_in, ax=ax, **kwargs)
        elif preset == 'line':
            ax = pyb.plots.lineplot(df_in, ax=ax, **kwargs)
        elif preset == 'line_fit':
            ax = pyb.plots.plot_line_fit(df_in, ax=ax, **kwargs)
        elif preset == 'scatter':
            ax = pyb.plots.scatterplot(df_in, ax=ax, **kwargs)
        elif preset == 'datapoints_and_mean':
            ax = pyb.plots.plot_datapoints_and_mean(df_in, dsList=dp.dsList, ax=ax, **kwargs)
        elif preset == 'heatmap':
            ax = pyb.plots.plot_heatmap(df_in, ax=ax, **kwargs)
        elif preset == 'timeseries':
            ax = pyb.plots.plot_timeseries(df_in, ax=ax, **kwargs)
        elif preset == 'boxplot':
            ax = pyb.plots.boxplot(df_in, ax=ax, **kwargs)
        elif preset == 'boxenplot':
            ax = pyb.plots.plot_boxenplot(df_in, ax=ax, **kwargs)
        elif preset == 'violinplot':
            ax = pyb.plots.violinplot(df_in, ax=ax, **kwargs)
        elif preset == 'spot_tracks':
            lineage = kwargs.pop('lineage', '')
            dp.fuse_columns(object_name=object_name, columns=['Idx', 'BacteriaLineage'], new='Track', inplace=True)
            if lineage:
                df_in = df_in.query('BacteriaLineage == @lineage')
            ax = pyb.plots.lineplot(df_in, hue='Track', sort=False, ax=ax, **kwargs)
        elif preset == 'rates_summary':
            ax = pyb.plots.plot_rates_summary(ax=ax, **kwargs)
        elif preset == 'grey_lines_and_highlight':
            ax = pyb.plots.plot_grey_lines_and_highlight(df_in, ax=ax, **kwargs)
        else:
            warn('Plot preset not found!')
        if return_axes:
            return ax
