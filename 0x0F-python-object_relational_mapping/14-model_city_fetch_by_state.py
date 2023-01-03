#!/usr/bin/python3
""" Using Relationship in SQLAlchemy

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City, Base, State


def fetch_city():
    """ Print all the cities in cities table """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).join(State).order_by(City.id):
        print(f"{city.state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    fetch_city()
