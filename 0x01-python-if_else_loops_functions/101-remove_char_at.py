#!/usr/bin/python3


def remove_char_at(str, n):
    """Removes the character at n position"""
    if (n < 0):
        return (str)
    s = ''
    i = 0
    while (i < len(str)):
        if (i == n):
            i += 1
            continue
        s += str[i]
        i += 1
    return (s)
