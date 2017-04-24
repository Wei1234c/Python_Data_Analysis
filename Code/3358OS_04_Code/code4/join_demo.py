import pandas as pd
from numpy.random import seed
from numpy.random import rand
from numpy.random import random_integers
import numpy as np

seed(42)

df = pd.DataFrame({'Weather' : ['cold', 'hot', 'cold', 'hot',
   'cold', 'hot', 'cold'],
   'Food' : ['soup', 'soup', 'icecream', 'chocolate',
   'icecream', 'icecream', 'soup'],
   'Price' : 10 * rand(7), 'Number' : random_integers(1, 9, size=(7,))})

print "df :3\n", df[:3]
print "Concat Back together\n", pd.concat([df[:3], df[3:]])

print "Appending rows\n", df[:3].append(df[5:])

dests = pd.read_csv('dest.csv')
print "Dests\n", dests

tips = pd.read_csv('tips.csv')
print "Tips\n", tips

print "Merge() on key\n", pd.merge(dests, tips, on='EmpNr')
print "Dests join() tips\n", dests.join(tips, lsuffix='Dest', rsuffix='Tips')

print "Inner join with merge()\n", pd.merge(dests, tips, how='inner')
print "Outer join\n", pd.merge(dests, tips, how='outer')
