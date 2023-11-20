#!/usr/bin/python3
"""
A script that Lists all City objects from the db
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).join(City).order_by(City.id).all()

    for s in states:
        for city in s.cities:
            print("{}: {} -> {}".format(city.id, city.name, s.name))
