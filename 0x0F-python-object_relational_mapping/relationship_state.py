#!/usr/bin/python3
""" Using the relationship property

"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """ A class Definition of the states table.

    """
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref=backref('state', order_by=id))
