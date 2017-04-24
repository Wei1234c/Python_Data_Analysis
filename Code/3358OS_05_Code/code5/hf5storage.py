import numpy as np
import tables
from tempfile import NamedTemporaryFile
from os.path import getsize

np.random.seed(42)
a = np.random.randn(365, 4)

tmpf = NamedTemporaryFile()
h5file = tables.openFile(tmpf.name, mode='w', title="NumPy Array")
root = h5file.root
h5file.createArray(root, "array", a)
h5file.close()

h5file = tables.openFile(tmpf.name, "r")
print getsize(tmpf.name)

for node in h5file.iterNodes(h5file.root):
   b = node.read()
   print type(b), b.shape
   
h5file.close()
