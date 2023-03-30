#!/usr/bin/python3
"""
Defines a State model.
Inherits from SQLAlchemy Base and links to the MySQL table states.
"""
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """
    State class that represents a state for MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name = (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement=True,
            unique=True
        )
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
