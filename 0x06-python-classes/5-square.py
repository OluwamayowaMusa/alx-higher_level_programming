#!/usr/bin/python3

""" A module which defines Square class.

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
        """ Gets the attribute size. Also checks for
        TypeError and ValueError
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """ Print a representation of the square """
        if self.__size != 0:
            i = 0
            while i < self.__size:
                print('#' * self.__size)
                i += 1
        else:
            print()
