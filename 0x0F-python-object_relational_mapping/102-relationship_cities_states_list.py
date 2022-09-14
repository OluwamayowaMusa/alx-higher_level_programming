#!/usr/bin/python3
""" Using the backref relationship

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base, State


def backref_property():
    """ Backref Property """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id):
        print(f"{city.id}: {city.name} -> {city.state.name}")


if __name__ == "__main__":
    backref_property()
