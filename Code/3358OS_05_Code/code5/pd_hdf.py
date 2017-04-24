import numpy as np
import pandas as pd
from tempfile import NamedTemporaryFile

np.random.seed(42)
a = np.random.randn(365, 4)

tmpf = NamedTemporaryFile()
store = pd.io.pytables.HDFStore(tmpf.name)
print store

df = pd.DataFrame(a)
store['df'] = df
print store

print "Get", store.get('df').shape
print "Lookup", store['df'].shape
print "Dotted", store.df.shape

del store['df']
print "After del\n", store

print "Before close", store.is_open
store.close()
print "After close", store.is_open

df.to_hdf(tmpf.name, 'data', format='table')
print pd.read_hdf(tmpf.name, 'data', where=['index>363'])
