#!/usr/bin/python3
""" Access a database from SQLAlchemy

"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}'
                       '@localhost/{}'.format(sys.argv[1],
                                              sys.argv[2], sys.argv[3]))

Session = sessionmaker(bind=engine)
session = Session()
for state in session.query(State).order_by(State.id):
    print(f"{state.id}: {state.name}")
