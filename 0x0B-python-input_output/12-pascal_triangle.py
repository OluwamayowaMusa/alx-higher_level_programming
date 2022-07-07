#!/usr/bin/python3
""" Defines a function that computes pascal triangle.

"""


def pascal_triangle(n):
    """ Computes pascal triangle.

    Args:
        n (int): Highest power in pascal triangle

    Returns:
        list of list of integers representing pascal triangle
    """

    if n <= 0:
        return []
    result = []
    for num in range(n):
        if num == 0:
            result.append([1])
        elif num == 1:
            result.append([1, 1])
        elif num > 1:
            j = 1
            temp = [1, 1]
            while j < len(result[-1]):
                temp.insert(j, result[-1][j - 1] + result[-1][j])
                j += 1
            result.append(temp)
    return result
