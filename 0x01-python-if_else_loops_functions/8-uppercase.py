#!/usr/bin/python3


def uppercase(str):
    """Prints string in uppercase"""

    for c in str:
        i = ord(c)
        if (97 <= i <= 122):
            i -= 32
            c = chr(i)
            print("{}".format(c), end='')
        else:
            print("{}".format(c), end='')
    print()
