#!/usr/bin/python3
""" Defines a function that returns the list of attributes of an object.

"""


def lookup(obj):
    """ Returns list of attributes and methods of an obj.

    Args:
        obj: Object

    Returns:
        List of attributes and methods
    """
    return dir(obj)
