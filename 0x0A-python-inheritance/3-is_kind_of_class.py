#!/usr/bin/python3
""" Defines a function that checks the object instance.

"""


def is_kind_of_class(obj, a_class):
    """ Checks if obj is an instance of a_class or subclass of a_class.

    """
    return isinstance(obj, a_class)
