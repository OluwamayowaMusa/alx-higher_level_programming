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
        return max(list_of_integers)
