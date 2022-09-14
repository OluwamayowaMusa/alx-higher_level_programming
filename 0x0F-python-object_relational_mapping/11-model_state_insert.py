#!/usr/bin/python3
""" Insert a new state in the table in database

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def insert_state():
    """ Insert a new state in table(states) """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_1 = State(name='Louisiana')
    session.add(state_1)
    session.commit()
    print(state_1.id)


if __name__ == "__main__":
    insert_state()
