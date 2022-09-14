#!/usr/bin/python3
""" Filtering the query using the filter method

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_sql():
    """ Use the filter method """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = sys.argv[4].split()[0]
    data = session.query(State).filter(State.name == user_input).first()
    if data:
        print(data.id)
    else:
        print('Not found')


if __name__ == "__main__":
    filter_sql()
