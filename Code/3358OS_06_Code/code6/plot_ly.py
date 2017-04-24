import plotly.plotly as py
from plotly.graph_objs import *
from getpass import getpass
import numpy as np
import pandas as pd

df = pd.read_csv('transcount.csv')
df = df.groupby('year').aggregate(np.mean)

gpu = pd.read_csv('gpu_transcount.csv')
gpu = gpu.groupby('year').aggregate(np.mean)

df = pd.merge(df, gpu, how='outer', left_index=True, right_index=True)
df = df.replace(np.nan, 0)

api_key = getpass()

# Change the user to your own username
py.sign_in('LearningPythonDataAnalysis', api_key)

counts = np.log(df['trans_count'].values)
gpu_counts = np.log(df['gpu_trans_count'].values)

data = Data([Box(y=counts), Box(y=gpu_counts)]) 
plot_url = py.plot(data, filename='moore-law-scatter')
print plot_url
