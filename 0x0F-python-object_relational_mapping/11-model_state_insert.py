#!/usr/bin/python3

"""
a script that adds the State object 'Louisiana'
to the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')

    session.add(new_state)
    new_unst = session.query(State).filter_by(name='Louisiana').first()

    print(new_unst.id)

    session.commit()
