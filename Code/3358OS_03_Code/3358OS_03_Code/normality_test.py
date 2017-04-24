import numpy as np
from scipy.stats import shapiro
from scipy.stats import anderson
from scipy.stats import normaltest



flutrends = np.loadtxt("goog_flutrends.csv", delimiter=',', usecols=(1,), skiprows=1, converters = {1: lambda s: float(s or 0)}, unpack=True)
N = len(flutrends)
normal_values = np.random.normal(size=N)
zero_values = np.zeros(N)

print "Normal Values Shapiro", shapiro(normal_values)
print "Zeroes Shapiro", shapiro(zero_values)
print "Flu Shapiro", shapiro(flutrends)
print

print "Normal Values Anderson", anderson(normal_values)
print "Zeroes Anderson", anderson(zero_values)
print "Flu Anderson", anderson(flutrends)
print

print "Normal Values normaltest", normaltest(normal_values)
print "Zeroes normaltest", normaltest(zero_values)
print "Flu normaltest", normaltest(flutrends)
