#!/usr/bin/python3
""" Find the peak in a list of unsorted integers

"""


def find_peak(list_of_integers):
    """ Find the maximum nuber

    Args:
        list_of_integers (list): List of numbers

    Return:
        Maximum number
    """
    if len(list_of_integers) == 0:
        return None
    else:
        for index, value in enumerate(list_of_integers):
            if index == 0 and value > list_of_integers[1]:
                return value
            elif index == len(list_of_integers) - 1:
                return value
            if index != 0:
                if value > list_of_integers[index - 1] and \
                     value > list_of_integers[index + 1]:
                    return value
