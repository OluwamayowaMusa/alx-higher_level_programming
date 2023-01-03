#!/usr/bin/python3
"""An  Object definition of the cities table in database

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """ The City table """
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'))

    state = relationship('State')
