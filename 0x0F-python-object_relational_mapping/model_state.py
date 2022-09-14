#!/usr/bin/python3
""" Using ORM to access a database (SQLAlchemy)

"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ A class Definition of the states table.

    """
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
