#!/usr/bin/python3

"""Defines a function that adds integers.

Example:
    >>> add_integer(2, 3)
    5
    >>> add_integer(4, 7)
    11
"""


def add_integer(a, b=98) -> int:
    """ Adds two integers.

    Args:
        a (int, float): First Number
        b (int, float): Second Number

    Return:
        Addition of a and b

    Raise:
        TypeError if a and b are not integers or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
