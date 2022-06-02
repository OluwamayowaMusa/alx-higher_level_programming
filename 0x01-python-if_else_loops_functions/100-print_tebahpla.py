#!/usr/bin/python3

i = 122  # ASCII value
ctrl = 1  # Control value
while (i > 96):
    if (ctrl == 0):
        i -= 32
    c = chr(i)
    print("{}".format(c), end='')
    if (ctrl == 0):
        i += 32
        ctrl = 1
    elif (ctrl == 1):
        ctrl = 0
    i -= 1
