#!/usr/bin/python3
""" Defines a function that checks the instance of an object.

"""


def is_same_class(obj, a_class):
    """ Checks if obj is exactly an instance of a_class.

    Args:
        obj: Object Passed
        a_class: Class Passed

    Returns:
        True is obj is exactly an instance of a_class
    """
    return type(obj) == a_class
