import numpy as np
import pandas as pd
from tempfile import NamedTemporaryFile
from os.path import getsize

np.random.seed(42)
a = np.random.randn(365, 4)

tmpf = NamedTemporaryFile()
np.savetxt(tmpf, a, delimiter=',')
print "Size CSV file", getsize(tmpf.name)

tmpf = NamedTemporaryFile()
np.save(tmpf, a)
tmpf.seek(0)
loaded = np.load(tmpf)
print "Shape", loaded.shape
print "Size .npy file", getsize(tmpf.name)

df = pd.DataFrame(a)
df.to_pickle(tmpf.name)
print "Size pickled dataframe", getsize(tmpf.name)
print "DF from pickle\n", pd.read_pickle(tmpf.name)
