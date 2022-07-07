#!/usr/bin/python3
""" Defines a function that writes object to a text file.

"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes object to a text file in JSON representation.

    Args:
        my_obj (any): Object passed
        filename (str): File name / path
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
