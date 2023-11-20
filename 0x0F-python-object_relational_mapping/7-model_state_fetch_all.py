#!/usr/bin/python3

"""
A script that lists all State objects
from the database `hbtn_0e_6_usa`.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """
    Access the database and get the states
    from the db.
    """

    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).order_by(State.id):
        print('{}: {}'.format(instance.id, instance.name))
