#!/usr/bin/python3
"""
Script that changes the name of a State object fro the database
hbtn_0e_6_usa.
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
    states = session.query(State).filter(State.id == 2).all()
    for state in states:
        state.name = 'New Mexico'
        session.commit()
    session.close()
