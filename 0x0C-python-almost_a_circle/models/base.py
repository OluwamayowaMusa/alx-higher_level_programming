#!/usr/bin/python3
""" Defines Base class.

"""


class Base:
    """ A base class for all other classes.

    Attributes:
        __nb_objects (private-int): Number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the object.

        Args:
            id (int): Id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
