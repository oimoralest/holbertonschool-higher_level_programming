#!/usr/bin/python3
"""
This modules define the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """
    This function computes the product between two matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row_a in m_a:
        if type(row_a) is not list:
            raise TypeError("m_a must be a list of lists")
    for row_b in m_b:
        if type(row_b) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row_a in m_a:
        for element_a in row_a:
            if type(element_a) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row_b in m_b:
        for element_b in row_b:
            if type(element_b) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    for row_a in m_a:
        if len(m_a[0]) != len(row_a):
            raise TypeError("each row of m_a must be of the same size")
    for row_b in m_b:
        if len(m_b[0]) != len(row_b):
            raise TypeError("each row of m_b must be of the same size")
    row_a = m_a[0]
    if len(row_a) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                matrix[i][j] += m_a[i][k] * m_b[k][j]
    return matrix
