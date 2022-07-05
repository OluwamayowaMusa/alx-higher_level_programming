#!/usr/bin/python3
""" Defines a class BaseGeometry.

"""


class BaseGeometry:
    """ An class which explains BaseGeometry.

    """

    def area(self):
        """ Raise Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates Value.

        Args:
            name (str): Type of value
            value (int): Size

        Raises:
            TypeError if value isn't an integer
            ValueError if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
