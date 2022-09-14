#!/usr/bin/python3
""" Using the first method of the query in SQLAlchemy

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_first():
    """ Get the first result of the query """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).first()
    if data:
        print(f"{data.id}: {data.name}")
    else:
        print('Nothing')


if __name__ == "__main__":
    filter_first()
