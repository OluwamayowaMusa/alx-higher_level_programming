#!/usr/bin/python3

""" A module which defines the Square class.

"""


class Square:
    """ Describes a Square.

    """

    def __init__(self, size=0):
        """ Initializes the object with size.

        Args:
            size (int): Size of square
        """
        self.size = size

    @property
    def size(self):
        """ Gets the size of the square. Also checks for
        TypeError and ValueError
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be a number")
        self.__size = value

    def area(self):
        """ Calculates the area of square"""
        return self.__size ** 2

    def __lt__(self, other):
        """ Checks if the area of object self is less than object other """
        return self.area() < other.area()

    def __le__(self, other):
        """ Checks if the area of object self is less than
        or equal to other area
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """ Checks if the area of object self is equal to
        object other area
        """
        return self.area() == other.area()

    def __nq__(self, other):
        """ Checks if the area of object self is not equal to
        object other area
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """ Checks if the area of object self is greater than
        object other area
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Checks if the area of object self is greater than
        or equal to object other area
        """
        return self.area() >= other.area()
