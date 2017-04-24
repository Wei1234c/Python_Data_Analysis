import Quandl

# Data from http://www.quandl.com/SIDC/SUNSPOTS_A-Sunspot-Numbers-Annual
# PyPi url https://pypi.python.org/pypi/Quandl
sunspots = Quandl.get("SIDC/SUNSPOTS_A")
print "Head 2", sunspots.head(2) 
print "Tail 2", sunspots.tail(2)

last_date = sunspots.index[-1]
print "Last value", sunspots.loc[last_date]

print "Values slice by date", sunspots["20020101": "20131231"]

print "Slice from a list of indices", sunspots.iloc[[2, 4, -4, -2]]

print "Scalar with Iloc", sunspots.iloc[0, 0]
print "Scalar with iat", sunspots.iat[1, 0]

print "Boolean selection", sunspots[sunspots > sunspots.mean()]
print "Boolean selection with column label", sunspots[sunspots.Number > sunspots.Number.mean()]
