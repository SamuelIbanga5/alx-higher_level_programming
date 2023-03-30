#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    passwd = args[2]
    dbname = args[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                user,
                passwd,
                dbname), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state = city.state
        print("{}: {} -> {}".format(city.id, city.name, state.name))
