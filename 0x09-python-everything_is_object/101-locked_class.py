#!/usr/bin/python3
""" A module which defines a locked class.

"""


class LockedClass:
    """ A class which prevent dynamic creation of instance attribute.

    """
    __slots__ = ["first_name"]
