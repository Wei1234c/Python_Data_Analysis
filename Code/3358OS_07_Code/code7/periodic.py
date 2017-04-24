from scipy.optimize import leastsq
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np


def model(p, t):
   C, p1, f1, phi1 , p2, f2, phi2, p3, f3, phi3 = p
   return C + p1 * np.sin(f1 * t + phi1) + p2 * np.sin(f2 * t + phi2) +p3 * np.sin(f3 * t + phi3)


def error(p, y, t):
   return y - model(p, t)

def fit(y, t):
   p0 = [y.mean(), 0, 2 * np.pi/11, 0, 0, 2 * np.pi/22, 0, 0, 2 * np.pi/100, 0]
   params = leastsq(error, p0, args=(y, t))[0]
   return params

data_loader = sm.datasets.sunspots.load_pandas()
sunspots = data_loader.data["SUNACTIVITY"].values
years = data_loader.data["YEAR"].values

cutoff = .9 * len(sunspots)
params = fit(sunspots[:cutoff], years[:cutoff])
print "Params", params

pred = model(params, years[cutoff:])
actual = sunspots[cutoff:]
print "Root mean square error", np.sqrt(np.mean((actual - pred) ** 2))
print "Mean absolute error", np.mean(np.abs(actual - pred))
print "Mean absolute percentage error", 100 * np.mean(np.abs(actual - pred)/actual)
mid = (actual + pred)/2
print "Symmetric Mean absolute percentage error", 100 * np.mean(np.abs(actual - pred)/mid)
print "Coefficient of determination", 1 - ((actual - pred) ** 2).sum()/ ((actual - actual.mean()) ** 2).sum()
year_range = data_loader.data["YEAR"].values[cutoff:]
plt.plot(year_range, actual, 'o', label="Sunspots")
plt.plot(year_range, pred, 'x', label="Prediction")
plt.grid(True)
plt.xlabel("YEAR")
plt.ylabel("SUNACTIVITY")
plt.legend()
plt.show()
