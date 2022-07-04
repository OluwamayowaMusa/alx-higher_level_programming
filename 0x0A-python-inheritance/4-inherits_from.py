#!/usr/bin/python3
""" Defines a function that checks the instance of object.

"""


def inherits_from(obj, a_class):
    """ Check if obj is an instance of a_class(directly or indirectly).

    Args:
        obj: Object Passed
        a_class: Class Passed

    Returns:
        True if obj is an instance of a_class(directly or indirectly)
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False
