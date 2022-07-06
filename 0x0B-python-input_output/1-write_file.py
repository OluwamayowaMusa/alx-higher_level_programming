#!/usr/bin/python3
""" Defines a function that writes to file.

"""


def write_file(filename="", text=""):
    """ Writes text to filename.

    Args:
        filename (str): File passed
        text (str): Text to write to file

    Return:
        number of characters written
    """

    if len(filename) != 0:
        with open(filename, 'w', encoding='utf-8') as f:
            no_chars = f.write(text)
        return no_chars
    return 0
