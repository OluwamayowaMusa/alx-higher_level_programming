#!/usr/bin/python3
""" Defines a function that converts a JSON string to Python object.

"""
import json


def from_json_string(my_str):
    """ Converts a JSON string to Python object.

    Args:
        my_str (str): JSON string

    Returns:
        Python object
    """
    return json.loads(my_str)
