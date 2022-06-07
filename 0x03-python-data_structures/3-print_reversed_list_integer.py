#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Print List in Reverse order"""
    if (my_list is not None):
        i = len(my_list) - 1
        while (i > -1):
            print("{:d}".format(my_list[i]))
            i -= 1


if (__name__ == "__main__"):
    print_reversed_list_integer(my_list)
