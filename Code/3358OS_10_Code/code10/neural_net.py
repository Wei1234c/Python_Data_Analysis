import numpy as np
import theanets
import multiprocessing
from sklearn import datasets
from sklearn.metrics import accuracy_score


rain = .1 * np.load('rain.npy')
rain[rain < 0] = .05/2
dates = np.load('doy.npy')
x = np.vstack((dates[:-1], np.sign(rain[:-1])))
x = x.T

y = np.vstack(np.sign(rain[1:]),)
N = int(.9 * len(x))

e = theanets.Experiment(theanets.Regressor,
                        layers=(2, 3, 1),
                        learning_rate=0.1,
                        momentum=0.5,
                        patience=300,
                        train_batches=multiprocessing.cpu_count(),
                        num_updates=500)

train = [x[:N], y[:N]]
valid = [x[N:], y[N:]]
e.run(train, valid)

pred = e.network(x[N:]).ravel()
print "Pred Min", pred.min(), "Max", pred.max()
print "Y Min", y.min(), "Max", y.max()
print "Accuracy", accuracy_score(y[N:], pred >= .5)
