#!/usr/bin/python3

""" Defines a function that print new lines after '.', '?' and ':'.

"""


def text_indentation(text):
    """ Prints new line after ., ? and :.

    Args:
        text (str): String passed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    _length = 0
    while _length < len(text):
        _c = text[_length]
        if _c in ".?:":
            print(_c, end='')
            print()
            print()
            while text[_length + 1] == ' ':
                _length +=1
        else:
            print(_c, end='')
        _length += 1
