import numpy as np
from rain import sum_rain

rain = np.load('../rain.npy')
print "Boost", sum_rain(rain.astype(int).tolist(), len(rain))
rain = .1 * rain
rain[rain < 0] = .025
print "Numpy", rain.sum()
