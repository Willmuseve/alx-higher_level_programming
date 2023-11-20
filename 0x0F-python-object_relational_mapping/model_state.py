#!/usr/bin/python3

"""
A script that defines a class State which is an instance
of Base=declarative_base() class
"""

from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class state which inherits from Base.
    Has an integer id and a name as a string
    """

    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
