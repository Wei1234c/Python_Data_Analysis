import numpy as np
import pandas as pd
from tempfile import NamedTemporaryFile

np.random.seed(42)
a = np.random.randn(365, 4)

tmpf = NamedTemporaryFile(suffix='.xlsx')
df = pd.DataFrame(a)
print tmpf.name
df.to_excel(tmpf.name, sheet_name='Random Data')
print "Means\n", pd.read_excel(tmpf.name, 'Random Data').mean()
