#!/usr/bin/python3

""" A module which defines a Square class.

"""


class Square:
    """ Describes a Square.

    """

    def __init__(self, size):
        """ Initializes the object with size.

        Args:
            size (int): Size of the square
        """
        self.size = size

    @property
    def size(self):
        """ Gets the size of the sqaure object. Also check the type
        of argument and return the right error
        """
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculates the area of the square"""
        return self.__size ** 2
