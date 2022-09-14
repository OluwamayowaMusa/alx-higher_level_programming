#!/usr/bin/python3
""" Using the relationship property

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, State, City


def relationship_property():
    """ Relationship """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(City).join(State).order_by(City.state_id).all()
    obj_dict = {}

    for obj in data:
        if obj.state not in obj_dict:
            obj_dict[obj.state] = []
            obj_dict[obj.state].append(obj)
        else:
            obj_dict[obj.state].append(obj)

    for key in obj_dict:
        print(f"{key.id}: {key.name}")
        for obj in obj_dict[key]:
            print(f"    {obj.id}: {obj.name}")


if __name__ == "__main__":
    relationship_property()
