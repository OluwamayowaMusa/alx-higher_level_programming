#!/usr/bin/python3
""" Defines a function that print square.

"""


def print_square(size):
    """ Prints a square of size passed.

    Args:
        size (int): Size length of square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    _length = 0
    while _length < size:
        print('#' * size)
        _length += 1
