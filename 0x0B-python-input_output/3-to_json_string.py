#!/usr/bin/python3
""" Defines a function that converts python object to JSON string.

"""
import json


def to_json_string(my_obj):
    """ Converts python object to JSON string.

    Args:
        my_obj (any): Python Object

    Returns:
        JSON representation of object
    """
    return json.dumps(my_obj)
