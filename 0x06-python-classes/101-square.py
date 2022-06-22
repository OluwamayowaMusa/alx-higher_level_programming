#!/usr/bin/python3

""" A module which defines a Square class.

"""


class Square:
    """ Describes a square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the object with size and position.

        Args:
            size (int): Size of the Square
            position (tuple): Position in space
        """
        self.size = size
        self.position = position

    def __str__(self):
        """ Prints the string representation of the object """
        _s = ''
        if self.__size != 0:
            i = 0
            while i < self.__position[1]:
                _s += '\n'
                i += 1
            i = 0
            while i < self.__size:
                if i != self.__size - 1:
                    _s += (' ' * self.__position[0] + '#' * self.__size + '\n')
                else:
                    _s += (' ' * self.__position[0] + '#' * self.__size)
                i += 1
        return _s

    @property
    def size(self):
        """ Gets the size of the square. Also
        checks the for TypeError and Value Eror
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Gets the position of square. Also
        check for TypeError
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculates the area of the square Object """
        return self.__size ** 2

    def my_print(self):
        """" Print the square with the character '#' to stdout """
        if self.__size != 0:
            i = 0
            while i < self.__position[1]:
                print()
                i += 1
            i = 0
            while i < self.__size:
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
                i += 1
        else:
            print()
