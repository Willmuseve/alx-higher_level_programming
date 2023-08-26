#!/usr/bin/python3

"""A python file that contains the class definition of a
State and an instance Base  declarative_base """

from sqlalchemy import create_engine, Sequence, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    __tableame__ = 'states'
    id = Column(
        Integer,
        Sequence('my_sequence'),
        primary_key=True,
        nullable=False
        )
    name = Column(String(128), nullable=False)
