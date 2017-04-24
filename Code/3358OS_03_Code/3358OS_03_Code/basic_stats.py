import numpy as np
from scipy.stats import scoreatpercentile

data = np.loadtxt("mdrtb_2012.csv", delimiter=',', usecols=(1,), skiprows=1, unpack=True)

print "Max method", data.max()
print "Max function", np.max(data)

print "Min method", data.min()
print "Min function", np.min(data)

print "Mean method", data.mean()
print "Mean function", np.mean(data)

print "Std method", data.std()
print "Std function", np.std(data)

print "Median", np.median(data)
print "Score at percentile 50", scoreatpercentile(data, 50)
