#!/usr/bin/pyhon3
""" A module which defines a class Rectangle.

"""


class Rectangle:
    """ Describes a Rectangle.

    """

    def __init__(self, width=0, height=0):
        """ Initializes the object.

        Args:
            width (int): Width of Reactangle
            height (int): Height of Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets the width of Rectangle. Raises TypeEror
        if width is not an integer, ValueError if width is
        not >= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height of rectangle. Raises TypeError
        if height is not an integer, ValueError if height is
        not >= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates the area of reactangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ String representation of object """
        if self.__width == 0 or self.__height == 0:
            return ""
        _s = ""
        i = 0
        while i < self.__height:
            _s += ('#' * self.__width + '\n')
            i += 1
        return _s[:-1]
