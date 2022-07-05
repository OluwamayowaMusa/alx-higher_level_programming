#!/usr/bin/python3
""" Defines a class that inherits from BaseGeometry.

"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ A class that inherits from class BaseGeometry.

    """

    def __init__(self, width, height):
        """ Initializes Object.

        Args:
            width(int): Size of width
            height (int): Size of height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ String repersentation of Class Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ Calculates the area of Rectangle """
        return self.__width * self.__height
