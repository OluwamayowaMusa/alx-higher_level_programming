#!/usr/bin/python3

""" A module which defines a Square class.
"""


class Square:
    """ A Square class with oject variable size.
    """

    def __init__(self, size=0):
        """ Initializes the object with size.

        Args:
            size (int): Size of the square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
