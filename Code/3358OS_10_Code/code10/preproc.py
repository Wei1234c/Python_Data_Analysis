import numpy as np
from sklearn import preprocessing
from scipy.stats import anderson


rain = np.load('rain.npy')
rain = .1 * rain
rain[rain < 0] = .05/2
print "Rain mean", rain.mean()
print "Rain variance", rain.var()
print "Anderson rain", anderson(rain)

scaled = preprocessing.scale(rain)
print "Scaled mean", scaled.mean()
print "Scaled variance", scaled.var()
print "Anderson scaled", anderson(scaled)

print len(rain[rain < 0])
binarized = preprocessing.binarize(rain)
print np.unique(binarized), binarized.sum()

lb = preprocessing.LabelBinarizer()
lb.fit(rain.astype(int))
print lb.classes_
