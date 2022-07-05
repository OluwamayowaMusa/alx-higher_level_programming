#!/usr/bin/python3
""" Defines a class Rectangle that inherit from BaseGeometry.

"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ A rectangle class that inherits from a class BaseGeometry.

    """

    def __init__(self, width, height):
        """ Initializes object.

        Args:
            width (int): Width of Object
            height (int): Height of Object
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
