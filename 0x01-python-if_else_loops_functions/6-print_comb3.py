#!/usr/bin/python3

i = 1
j = 2
while (i < 90):
    if (i != 89):
        if (i % 10 != 9):
            print("{:02d}, ".format(i), end='')
        else:
            print("{:02d}, ".format(i), end='')
            i += j + 1
            j += 1
            continue
    else:
        print("{:02d}".format(i))
    i += 1
