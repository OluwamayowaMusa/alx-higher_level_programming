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
        start = 0
        end = len(list_of_integers) - 1
        if list_of_integers[start] > list_of_integers[start + 1]:
            return list_of_integers[start]
        elif list_of_integers[end] > list_of_integers[end - 1]:
            return list_of_integers[end]

        while start < end:
            mid = int((end + start) / 2)

            if list_of_integers[mid - 1] <= list_of_integers[mid] >= \
                    list_of_integers[mid + 1]:
                return list_of_integers[mid]

            if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
                end = mid
            else:
                start = mid + 1
