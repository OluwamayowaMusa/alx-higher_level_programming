#!/usr/bin/python3
""" Update a row in the table in database

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_row():
    """ Update table in database """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).filter(State.id == 2).first()
    data.name = 'New Mexico'
    session.commit()


if __name__ == "__main__":
    update_row()
