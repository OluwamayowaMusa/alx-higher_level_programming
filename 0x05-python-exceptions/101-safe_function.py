#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """ Execute a function safely"""

    try:
        result = fct(*args)
        return (result)
    except BaseException as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (None)
