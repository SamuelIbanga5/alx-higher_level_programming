#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
container in the database hbtn_0e_101_usa.
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
    states = session.query(State).order_by(State.id).all()
    for state in states:
        cities = state.cities
        print("{}: {}".format(state.id, state.name))
        for city in cities:
            print("\t{}: {}".format(city.id, city.name))
