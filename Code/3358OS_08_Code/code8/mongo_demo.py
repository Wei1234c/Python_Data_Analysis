from pymongo import MongoClient
import statsmodels.api as sm
import json
import pandas as pd


client = MongoClient()
db = client.test_database

data_loader = sm.datasets.sunspots.load_pandas()
df = data_loader.data
rows = json.loads(df.T.to_json()).values()
db.sunspots.insert(rows)

cursor = db['sunspots'].find({})
df =  pd.DataFrame(list(cursor))
print df

db.drop_collection('sunspots')
