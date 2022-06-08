#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns the key with the biggest value"""
    if (a_dictionary is None):
        return (None)
    if (len(a_dictionary) == 0):
        return (None)
    keyList = list(a_dictionary.keys())
    valList = list(a_dictionary.values())
    maxVal = max(valList)
    index = valList.index(maxVal)
    return (keyList[index])
