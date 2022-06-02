#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end=' ')

if (number >= 0):
    lastDigit = number % 10
else:
    lastDigit = number % 10
    if (lastDigit != 0):
        lastDigit -= 10

if (lastDigit > 5):
    print(f"{lastDigit} and is greater than 5")
elif (lastDigit == 0):
    print(f"{lastDigit} and is 0")
else:
    print(f"{lastDigit} and is less than 6 and not 0")
