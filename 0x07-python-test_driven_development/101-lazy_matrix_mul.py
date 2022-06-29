#!/usr/bin/python3
""" Defines a function that uses `numpy` to multiply matrix.

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiplys two matrices.

    Args:
        m_a (list of lists): First Matrix
        m_b (list of lists): Second Matrix

    Return:
        Multiplication of both martrices
    """

    if type(m_a) is not list or type(m_b) is not list:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    h_a = len(m_a)
    w_a = 0 if h_a == 0 else len(m_a[0])
    h_b = len(m_b)
    w_b = 0 if h_b == 0 else len(m_b[0])

    if h_a == 0 or w_a == 0 or h_b == 0 or w_b == 0:
        raise ValueError("shapes ({:d},{:d}) and ({:d}, {:d}) not aligned:"
                         " {:d} (dim {:d})!= {:d} (dim {:d})".format(h_a, w_a,
                                                                      h_a, w_b,
                                                                      w_a, h_a,
                                                                      w_b, w_a)
                         )

    for r_a in m_a:
        if len(r_a) != len(m_a[0]):
            raise ValueError("setting an array element with a sequence.")
        for c_a in r_a:
            if type(c_a) is not int and type(c_a) is not float:
                raise TypeError("invalid data type for einsum")
    for r_b in m_b:
        if len(r_b) != len(m_b[0]):
            raise ValueError("setting an array element with a sequnece.")
        for c_b in r_b:
            if type(c_b) is not int and type(c_b) is not float:
                raise TypeError("invalid data type for einsum")
    if len(m_a[0]) != len(m_b):
        raise ValueError("shapes ({:d},{:d}) and ({:d}, {:d}) not aligned:"
                         " {:d} (dim {:d})!= {:d} (dim {:d})".format(w_b, h_a,
                                                                      w_b, w_b,
                                                                      h_a, h_b,
                                                                      w_b, h_a)
                         )

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for inner_list in m_a:
        if not isinstance(inner_list, list):
            raise TypeError("m_a must be a list of lists")
    for inner_list in m_b:
        if not isinstance(inner_list, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for inner_list in m_a:
        for num in inner_list:
            if not isinstance(num, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for inner_list in m_b:
        for num in inner_list:
            if not isinstance(num, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    for inner_list in m_a:
        if len(m_a[0]) != len(inner_list):
            raise TypeError("each row of m_a must be of the same size")
    for inner_list in m_b:
        if len(m_b[0]) != len(inner_list):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return np.matmul(np.array(m_a), np.array(m_b))
