from pandas.io.parsers import read_csv

df = read_csv("WHO_first9cols.csv")
print "Dataframe", df
print "Shape", df.shape
print "Length", len(df)
print "Column Headers", df.columns
print "Data types", df.dtypes
print "Index", df.index
print "Values", df.values
