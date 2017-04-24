import pandas as pd
from numpy.random import seed
from numpy.random import rand
from numpy.random import random_integers
import numpy as np

seed(42)
N = 7
df = pd.DataFrame({
   'Weather' : ['cold', 'hot', 'cold', 'hot',
   'cold', 'hot', 'cold'],
   'Food' : ['soup', 'soup', 'icecream', 'chocolate',
   'icecream', 'icecream', 'soup'],
   'Price' : 10 * rand(N), 'Number' : random_integers(1, 9, size=(N,))})

print "DataFrame\n", df
print pd.pivot_table(df, cols=['Food'], aggfunc=np.sum)
