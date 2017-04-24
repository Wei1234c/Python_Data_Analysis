from pony.orm import Database, db_session 
from pandas.io.sql import write_frame
import statsmodels.api as sm

db = Database('sqlite', ':memory:')

with db_session:
    data_loader = sm.datasets.sunspots.load_pandas()
    df = data_loader.data
    write_frame(df, "sunspots", db.get_connection()) 
    print db.select("count(*) FROM sunspots")
