#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Print the first 'x' elements of a list and only integers"""

    i = 0
    j = 0
    while (i < x):
        try:
            val = my_list[i]
            print("{:d}".format(val), end='')
            i += 1
        except (ValueError, TypeError):
            pass
            i += 1
            j += 1
    print()
    return (i - j)


if (__name__ == "__main__"):
    safe_print_list_integers()
