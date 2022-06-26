#!/usr/bin/python3
""" Defines a function that multiplies two matrices.

"""


def matrix_mul(m_a, m_b):
    """ Multiplies two matrices (list of lists).

    Args:
        m_a (list of lists): First Matrix
        m_b (list of lists): Second Matrix

    Return:
        Multiplication of both matrices
    """

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

    result_list = []
    for i in range(len(m_a)):
        temp = []
        j = 0
        while j < len(m_b):
            k, num = 0, 0
            while k < len(m_b):
                num += m_a[i][k] * m_b[k][j]
                k += 1
            j += 1
            temp.append(num)
        result_list.append(temp)
    return result_list
