#!/usr/bin/python3
"""
a script defines a City class
to work with MySQLAlchemy ORM.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ (str): table name of the class
        id (int): class id
        name (str): class name
        state_id (int): The state the city is in
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
