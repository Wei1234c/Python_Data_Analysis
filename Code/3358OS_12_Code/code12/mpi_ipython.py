from mpi4py import MPI
from numpy.random import random_integers
from numpy.random import randn
import numpy as np
import statsmodels.api as sm
import bottleneck as bn
import logging


def jackknife(a, parallel=True):
    data_loader = sm.datasets.sunspots.load_pandas()
    vals = data_loader.data['SUNACTIVITY'].values

    func, _ = bn.func.nanmean_selector(vals, axis=0)
    results = []

    for i in a:
        tmp = np.array(vals.tolist())
        tmp[i] = np.nan
        results.append(func(tmp))

    results = np.array(results)

    if parallel:
        comm = MPI.COMM_WORLD
        rcvBuf = np.zeros(0.0, 'd')
        comm.gather([results, MPI.DOUBLE], [rcvBuf, MPI.DOUBLE])

    return results

if __name__ == "__main__":
    skiplist = np.arange(39, dtype='int')
    print jackknife(skiplist, False)
    
