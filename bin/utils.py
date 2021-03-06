import os, errno, sys
import h5py
import numpy as np

def prepare_output_file(filename):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise e

def read_hdf5(filename, datasets):
    import h5py
    f = h5py.File(filename, 'r')
    if isinstance(datasets, list) or isinstance(datasets, tuple):
        data = []
        for dataset in datasets:
            data.append(f[dataset][:])
    else:
        data = f[datasets][:]
    f.close()
    return data

def array_lookup(mapping, keys):
    """
    Get indices of matched strings in a numpy array
    :param mapping: a 1D array of strings
    :param keys: a 1D array of keys to lookup
    :return: a 1D array of indices of keys
    """
    d = {k: i for i, k in enumerate(mapping)}
    return np.asarray([d[k] for k in keys])