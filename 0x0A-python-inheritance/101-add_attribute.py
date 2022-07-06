#!/usr/bin/python3
""" Defines a function that adds attribute to a class.

"""


def add_attribute(object_, attr, value):
    """ Adds attribute to object_.

    Args:
        object_: Object
        attr: attribute
        value: value
    """
    if isinstance(object_, (str, int, list, float, dict, tuple)):
        raise TypeError("can't add new attribute")
    setattr(object_, attr, value)
