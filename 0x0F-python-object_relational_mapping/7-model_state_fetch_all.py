#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
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
                dbname),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
