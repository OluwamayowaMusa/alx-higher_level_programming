#!/usr/bin/python3
""" Delete a row from a table ina database

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_row():
    """ Delete record from table """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State):
        if 'a' in state.name:
            session.delete(state)
    session.commit()


if __name__ == "__main__":
    delete_row()
