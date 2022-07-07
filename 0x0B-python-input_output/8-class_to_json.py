#!/usr/bin/python3
""" Defines a function that returns dictionary desciption of an object.

"""


def class_to_json(obj):
    """ Dictionary representation of an object.

    Args:
        obj (any): Object passed

    Returns:
        Dictionary representation of an object
    """
    return obj.__dict__
