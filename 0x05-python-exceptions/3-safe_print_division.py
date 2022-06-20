#!/usr/bin/pyhon3


def safe_print_division(a, b):
    """Divides 2 integers and print the result"""

    try:
        val = a / b
    except ZeroDivisionError:
        val = None
        pass
    finally:
        print("Inside result: {}".format(val))
        return (val)
