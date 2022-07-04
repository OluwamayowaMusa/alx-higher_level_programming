#!/usr/bin/python3
""" Defines a class MyList that inherits from list.

"""


class MyList(list):
    """ A class that inherits from List.

    """

    def print_sorted(self):
        """ Print list in sorted ascending order """
        print(sorted(self))
