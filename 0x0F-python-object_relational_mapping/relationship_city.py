#!/usr/bin/python3
"""
Defines City model.
Inherits from SQLAlchemy Base and links to the MySQL table cities.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City class that represents a city for MySQL database.

    __tablename__ (str): Name of the MySQL table to store Cities.
    id (sqlalchemy.Integer): represents cities id.
    name (sqlalchemy.String): represents name of city.
    state_id (sqlalchemy.Integer): represents states id that is
    related to city.
    """
    __tablename__ = 'cities'
    id = Column(
            Integer,
            primary_key=True,
            unique=True,
            autoincrement=True,
            nullable=False
            )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
