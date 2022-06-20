#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """ Prints x elements of a list """
    i = 0
    while (i < x):
        try:
            val = my_list[i]
            print(val, end='')
            i += 1
        except IndexError:
            break
    print()
    return (i)


if (__name__ == "__main__"):
    safe_print_list()
