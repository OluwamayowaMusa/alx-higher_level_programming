#!/usr/bin/python3
""" FIltering the result based on a condition

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_cond():
    """ Filter the result """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for states in session.query(State):
        if 'a' in states.name:
            print(f"{states.id}: {states.name}")


if __name__ == "__main__":
    filter_cond()
