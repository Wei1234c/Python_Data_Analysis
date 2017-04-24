import statsmodels.api as sm
from pandas.io.sql import read_sql
import sqlite3

with sqlite3.connect(":memory:") as con:
    c = con.cursor()

    data_loader = sm.datasets.sunspots.load_pandas()
    df = data_loader.data
    rows = [tuple(x) for x in df.values]

    con.execute("CREATE TABLE sunspots(year, sunactivity)")
    con.executemany("INSERT INTO sunspots(year, sunactivity) VALUES (?, ?)", rows)
    c.execute("SELECT COUNT(*) FROM sunspots")
    print c.fetchone()
    print "Deleted", con.execute("DELETE FROM sunspots where sunactivity > 20").rowcount, "rows"

    print read_sql("SELECT * FROM sunspots where year < 1732", con)
    con.execute("DROP TABLE sunspots")

    c.close()
