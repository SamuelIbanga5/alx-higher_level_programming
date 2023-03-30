#!/usr/bin/python3
"""
Script that creates the State "California" with the City
"San Francisco" from the database hbtn_0e_100_usa.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    passwd = args[2]
    dbname = args[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                user,
                passwd,
                dbname), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
