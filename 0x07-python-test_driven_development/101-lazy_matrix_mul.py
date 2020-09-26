#!/usr/bin/python3
"""
This module defines the function lazy_matrix_mul
"""


def lazy_matrix_mul(m_a, m_b):
    """
    This function uses the numpy module to compute the product of two matrices
    """
    import numpy
    return numpy.matmul(m_a, m_b)
