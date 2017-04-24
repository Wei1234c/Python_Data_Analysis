from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import statsmodels.api as sm

cluster = Cluster()
session = cluster.connect()
session.execute("CREATE KEYSPACE IF NOT EXISTS mykeyspace WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };")
session.set_keyspace('mykeyspace')
session.execute("CREATE TABLE IF NOT EXISTS sunspots (year decimal PRIMARY KEY, sunactivity decimal);")

query = SimpleStatement(
    "INSERT INTO sunspots (year, sunactivity) VALUES (%s, %s)",
    consistency_level=ConsistencyLevel.QUORUM)

data_loader = sm.datasets.sunspots.load_pandas()
df = data_loader.data
rows = [tuple(x) for x in df.values]

for row in rows:
    session.execute(query, row)

print session.execute("SELECT COUNT(*) FROM sunspots")

session.execute('DROP KEYSPACE mykeyspace') 
cluster.shutdown()
