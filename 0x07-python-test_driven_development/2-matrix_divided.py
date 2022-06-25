#!/usr/bin/python3

""" Defines a function which divides the elements of matrix by a number.

Example:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """ Divides a matrix by number.

    Args:
        matrix (list of lists): Matrix of numbers
        div (int): Number

    Return:
        A new matrix

    Raise:
        TypeError if div isn't a number
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for inner_matrix in matrix:
        for _num in inner_matrix:
            if not isinstance(_num, (int, float)):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
    len_of_row = len(matrix[0])
    for inner_matrix in matrix:
        if len(inner_matrix) != len_of_row:
            raise TypeError("Each row of the matrix must have the same size")
    _temp = []
    for inner_matrix in matrix:
        _temp1 = []
        for _num in inner_matrix:
            _temp1.append(round(_num / div, 2))
        _temp.append(_temp1)

    return _temp
