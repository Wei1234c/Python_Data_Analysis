import Quandl

# Data from http://www.quandl.com/SIDC/SUNSPOTS_A-Sunspot-Numbers-Annual
# PyPi url https://pypi.python.org/pypi/Quandl
sunspots = Quandl.get("SIDC/SUNSPOTS_A")
print "Describe", sunspots.describe()
print "Non NaN observations", sunspots.count()
print "MAD", sunspots.mad()
print "Median", sunspots.median()
print "Min", sunspots.min()
print "Max", sunspots.max()
print "Mode", sunspots.mode()
print "Standard Deviation", sunspots.std()
print "Variance", sunspots.var()
print "Skewness", sunspots.skew()
print "Kurtosis", sunspots.kurt()
