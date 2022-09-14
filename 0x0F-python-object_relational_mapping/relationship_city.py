#!/usr/bin/python3
""" Use the relationship property

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from relationship_state import Base, State


class City(Base):
    """ The City table """
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'))
