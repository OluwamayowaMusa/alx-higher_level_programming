#!/usr/bin/python3
""" Defines a function that append to a file.

"""


def append_write(filename='', text=''):
    """ Appends text to filename.

    Args:
        filename (str): Filename
        text (str): Text to append to file

    Returns:
        Number of characters added to file
    """

    if len(filename) != 0:
        with open(filename, 'a', encoding='utf-8') as f:
            no_chars = f.write(text)
        return no_chars
    return 0
