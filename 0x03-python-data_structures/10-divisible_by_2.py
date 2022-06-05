#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Find all Multiples of 2"""

    if (len(my_list) == 0):
        return (None)
    rList = []
    for i in my_list:
        if (i % 2 == 0):
            rList.append(True)
        else:
            rList.append(False)
    return (rList)
