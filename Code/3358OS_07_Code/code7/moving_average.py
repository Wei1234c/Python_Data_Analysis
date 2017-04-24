import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas.stats.moments import rolling_mean

data_loader = sm.datasets.sunspots.load_pandas()
df = data_loader.data
year_range = df["YEAR"].values
plt.plot(year_range, df["SUNACTIVITY"].values, label="Original")
plt.plot(year_range, rolling_mean(df, 11)["SUNACTIVITY"].values, label="SMA 11")
plt.plot(year_range, rolling_mean(df, 22)["SUNACTIVITY"].values, label="SMA 22")
plt.legend()
plt.show()
