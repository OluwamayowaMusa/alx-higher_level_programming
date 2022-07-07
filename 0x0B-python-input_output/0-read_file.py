#!/usr/bin/python3
""" Defines a function that reads a text file.

"""


def read_file(filename=''):
    """ Reads a text file and prints to stdout.

    Args:
        filename (str): File name / path
    """

    if len(filename) != 0:
        with open(filename, 'r', encoding='utf-8') as f:
            read_data = f.read()
        print(read_data, end='')
