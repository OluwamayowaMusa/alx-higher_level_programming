#!/usr/bin/python3


def max_integer(my_list=[]):
    """Biggest Integer of a List"""

    if (len(my_list) == 0):
        return (None)

    maxNum = None
    for i in range(0, len(my_list)):
        if (i == 0):
            maxNum = my_list[0]
        else:
            if (maxNum < my_list[i]):
                maxNum = my_list[i]
    return (maxNum)
