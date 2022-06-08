#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """Delete keys with specific value"""
    keysList = list(a_dictionary.keys())
    vaList = list(a_dictionary.values())
    if (value not in vaList):
        return (a_dictionary)

    while (value in vaList):
        index = vaList.index(value)
        del a_dictionary[keysList[index]]
        vaList.remove(value)
        keysList.remove(keysList[index])

    return (a_dictionary)
