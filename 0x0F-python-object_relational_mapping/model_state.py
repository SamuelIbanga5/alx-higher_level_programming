#!/usr/bin/python3
"""
File that contains the class definition of a state and an instance\
Base = declarative_base().
"""
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    Base = declarative_base()

    class State(Base):
        """
        State class that defines the states model for MySQL database.
        """
        __tablename__ = 'states'
        id = Column(
                Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True,
                unique=True
            )
        name = Column(String(128), nullable=False)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                'Ibangajnr',
                'software',
                'hbtn_0e_6_usa'), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
