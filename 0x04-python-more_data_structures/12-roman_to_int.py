#!/usr/bin/python3


def roman_to_int(roman_string):
    """Converts roman string to number"""
    if (roman_string is None):
        return (0)
    romanDict = {'I': 1, "IV": 4, 'V': 5, "IX": 9, 'X': 10,
                 "XL": 40, 'L': 50, "XC": 90, 'C': 100, "CD": 400,
                 'D': 500, "CM": 900, 'M': 1000}
    abNom = ["IV", "IX", "XL", "XC", "CD", "CM"]
    num = start = i = 0
    end = 2
    while (i < len(roman_string)):
        if (len(roman_string) == 1):
            return (romanDict[roman_string])
        else:
            if (roman_string[start:end] in abNom):
                num += romanDict[roman_string[start:end]]
                i += 2
                start += 2
                end += 2
                continue
            num += romanDict[roman_string[i]]
            start += 1
            end += 1
            i += 1
    return (num)
