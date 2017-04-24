import pandas as pd
import numpy as np

df = pd.read_csv('WHO_first9cols.csv')
# Select first 3 rows of country and Net primary school enrolment ratio male (%)
df = df[['Country', df.columns[-2]]][:2]
print "New df\n", df
print "Null Values\n", pd.isnull(df)
print "Total Null Values\n", pd.isnull(df).sum()
print "Not Null Values\n", df.notnull()
print "Last Column Doubled\n", 2 * df[df.columns[-1]]
print "Last Column plus NaN\n", df[df.columns[-1]] + np.nan
print "Zero filled\n", df.fillna(0)
