import pandas as pd
from pandas.tseries.offsets import DateOffset
import sys

print "Date range", pd.date_range('1/1/1900', periods=42, freq='D')

try:
   print "Date range", pd.date_range('1/1/1677', periods=4, freq='D')
except:
   etype, value, _ = sys.exc_info()
   print "Error encountered", etype, value

offset = DateOffset(seconds=2 ** 63/10 ** 9)
mid = pd.to_datetime('1/1/1970')
print "Start valid range", mid - offset
print "End valid range", mid + offset
print pd.to_datetime(['1900/1/1', '1901.12.11'])

print "With format", pd.to_datetime(['19021112', '19031230'], format='%Y%m%d')

print "Illegal date", pd.to_datetime(['1902-11-12', 'not a date'])
print "Illegal date coerced", pd.to_datetime(['1902-11-12', 'not a date'], coerce=True)


   
