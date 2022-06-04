#!/usr/bin/python3

if (__name__ != "__main__"):
    for i in range(65, 91):
        c = chr(i)
        if (i != 90):
            print("{}".format(c), end='')
        else:
            print("{}".format(c))
