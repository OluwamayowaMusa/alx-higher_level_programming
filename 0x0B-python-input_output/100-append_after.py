#!/usr/bin/python3
""" Defines a function that inserts line in a text file.

"""


def append_after(filename='', search_string='', new_string=''):
    """ Inserts line in a text file.

    Inserts line in a text file after a line containing a specific
    string.

    Args:
        filename (str): Filename / file path
        search_string (str): Specific string
        new_string (str): New string to add to text file
    """

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines_copy = lines[:]
    i = 1
    for index, line in enumerate(lines):
        if search_string in line:
            lines_copy.insert(index + i, new_string)
            i += 1

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines_copy)
