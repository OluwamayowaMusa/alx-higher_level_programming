#!/usr/bin/python3
""" Defines a class which inherits from Class Rectangle.

"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle.

    """

    def __init__(self, size):
        """ Initializes Object.

        Args:
            size (int): Size of object

        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Calculates Area square """
        return self.__size ** 2
