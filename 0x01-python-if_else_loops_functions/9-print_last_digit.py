#!/usr/bin/python3


def print_last_digit(number):
    """Print last digit"""
    lastDigit = number % 10
    if (number < 0):
        if(lastDigit != 0):
            lastDigit -= 10
            lastDigit *= -1
    print(lastDigit, end='')
    return (lastDigit)
