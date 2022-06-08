#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Return a matrix with all elements square"""

    def square(x): return (x ** 2)
    rList = [list(map(square, i)) for i in matrix]
    return (rList)
