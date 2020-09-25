#!/usr/bin/python3
"""
This module defines a function matrix_divided


"""


def matrix_divided(matrix, div):
    """
    This function divides each element of a matrix by a number
    """
    if matrix and type(matrix) is list and type(matrix[0]) is list and \
       len(matrix[0]) != 0:
        _len = len(matrix[0])
        for row in matrix:
            if type(row) is list:
                if len(row) != _len:
                    raise TypeError("Each row of the matrix must have the \
same size")
                for elem in row:
                    if type(elem) is not int and type(elem) is not float:
                        raise TypeError("matrix must be a matrix (list of \
lists) of integers/floats")
                _len = len(row)
            else:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if div != 0 and (type(div) is int or type(div) is float):
            new = []
            new = [[round(elem / div, 2) for elem in row] for row in matrix]
            return new
        elif div == 0:
            raise ZeroDivisionError("division by zero")
        else:
            raise TypeError("div must be a number")
    elif type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    elif len(matrix) != 0 and type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    elif len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
