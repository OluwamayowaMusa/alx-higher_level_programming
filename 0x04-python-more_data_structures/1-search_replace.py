#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replace of all occurences of an element
        by another in a new list
    """
    tempList = my_list[:]
    for index, i in enumerate(tempList):
        if (i == search):
            tempList[index] = replace
    return (tempList)
