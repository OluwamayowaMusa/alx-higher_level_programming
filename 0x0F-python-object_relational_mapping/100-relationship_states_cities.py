#!/usr/bin/python3
""" Create a record in a table in database

"""
import sys
from relationship_city import City, Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def relationship_table():
    """ Add a record to a database table """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_1 = State(name='California')
    session.add(state_1)
    session.commit()
    state_1.cities.append(City(name='San Francisco'))
    session.commit()


if __name__ == "__main__":
    relationship_table()
