#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_city import City
from model_state import Base, State

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
    states = session.query(
            State,
            City).filter(
                    City.state_id == State.id
                ).order_by(
                    City.id
                    ).all()
    for state, city in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
