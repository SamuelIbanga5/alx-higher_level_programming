#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
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
                dbname), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    states = session.query(State).\
        order_by(State.id).filter(State.name.contains('a')).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
