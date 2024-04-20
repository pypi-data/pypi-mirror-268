import json
from os.path import join, exists
import pandas as pd


def read_config(ds_path, ds):
    config = dict()
    cf = join(ds_path, ds, f"{ds}_config.json")
    assert exists(cf), f'Config file for dataset {ds} not found'
    with open(cf, errors='ignore') as f:
        conf = json.load(f)
        config['object_class_names'] = [c["name"] for c in conf["structures"]]
        config['object_parents'] = [c["parentStructure"] for c in conf["structures"]]
        config['channelImage'] = [c["channelImage"][0] for c in conf["structures"]]
        if 'positionName' in conf['positions'][0]['images'].keys():
            config['positions'] = [c['images']['positionName'] for c in conf['positions']]
        else:
            config['positions'] = [c['images']['name'] for c in conf['positions']]
        config['dupChannels'] = conf['channelImagesDuplicated']
    return config


def read_metadata(ds_path, ds, pos):
    metadata = dict()
    path = join(ds_path, ds, 'SourceImageMetadata', f"{pos}.json")
    with open(path, errors='ignore') as f:
        file = json.load(f)
        for ch, data in file.items():
            metadata[ch] = (pd.json_normalize(data)
                            .reset_index(names='Frame')
                            .assign(Dataset=ds,
                                    Position=pos
                                    )
                            )
    return metadata


def dict_val_to_list(dict_in):
    for key, val in dict_in.items():
        dict_in[key] = arg_to_list(val)
    return dict_in


def arg_to_list(arg_in):
    if type(arg_in) is list:
        return arg_in
    else:
        return [arg_in]
