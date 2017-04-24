import bottleneck as bn
import numpy as np
import timeit


setup = '''
import numpy as np
import bottleneck as bn
from scipy.stats import rankdata

np.random.seed(42)
a = np.random.randn(30)
'''
def time(code, setup, n):
    return timeit.Timer(code, setup=setup).repeat(3, n)

if __name__ == '__main__':
    n = 10**3
    print n, "pass", max(time("pass", "", n))
    print n, "min np.median", min(time('np.median(a)', setup, n))
    print n, "min bn.median", min(time('bn.median(a)', setup, n))
    a = np.arange(7)
    print "Median diff", np.median(a) - bn.median(a)
    func, _ = bn.func.median_selector(a, axis=0)
    print "Bottleneck median func name", func

    print n, "min scipy.stats.rankdata", min(time('rankdata(a)', setup, n))
    print n, "min bn.rankdata", min(time('bn.rankdata(a)', setup, n))
    func, _ = bn.func.rankdata_selector(a, axis=0)
    print "Bottleneck rankdata func name", func
