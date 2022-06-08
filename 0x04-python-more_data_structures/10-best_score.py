#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns the key with the biggest value"""
    if (a_dictionary is None):
        return (None)
    if (len(a_dictionary) == 0):
        return (None)
    keyList = list(a_dictionary.keys())
    valList = list(a_dictionary.values())
    maxval = None
    res = None
    if (len(valList) == 0):
        return (None)
    for index, i in enumerate(valList):
        if (index == 0):
            maxVal = i
        else:
            if (i > maxVal):
                maxVal = i
                res = index
    if (valList.count(maxVal) != 1):
        return (None)
    return (keyList[res])
