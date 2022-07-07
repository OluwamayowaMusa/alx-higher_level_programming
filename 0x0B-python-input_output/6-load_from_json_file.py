#!/usr/bin/python3
""" Defines a function that creates object from JSON file.

"""
import json


def load_from_json_file(filename):
    """ Creates object from JSON file.

    Args:
        filename (str): Name of JSON file

    Returns:
        Object created
    """
    with open(filename, 'r', encoding='utf-8') as f:
        obj = json.load(f)
    return obj
