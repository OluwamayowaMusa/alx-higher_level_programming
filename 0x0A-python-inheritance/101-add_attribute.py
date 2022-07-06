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
    if type(object_) in (str, int, list, float, dict, tuple):
        raise TypeError("can't add new attribute")
    if hasattr(object_, "__slots__"):
        if attr not in object_.__slots__:
            raise TypeError("can't add new attribute")
    setattr(object_, attr, value)
