from alchemy_entities import Base, Sensor, Station
from populate_db import populate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from pandas.io.sql import read_sql


engine = create_engine('sqlite:///demo.db')
Base.metadata.create_all(engine)
populate(engine)
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

station = session.query(Station).first()

print "Query 1", session.query(Station).all()
print "Query 2", session.query(Sensor).all()
print "Query 3", session.query(Sensor).filter(Sensor.station == station).one()
print read_sql("SELECT * FROM station", engine.raw_connection())

try:
    os.remove('demo.db')
    print "Deleted demo.db"
except OSError:
    pass
