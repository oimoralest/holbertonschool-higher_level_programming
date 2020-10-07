#!/usr/bin/python3
"""
This module defines pascal_triangle function
"""


def pascal_triangle(n):
    """
    that returns a list of lists of integers representing the Pascal’s
    triangle of n
    """
    triangle = []
    i = 0
    if n >= 1:
        triangle.append([1])
        i += 1
        if n >= 2:
            triangle.append([1, 1])
            i += 1
            if n > 2:
                while i < n:
                    _list = []
                    _list.append(triangle[i - 1][0])
                    for j in range(len(triangle[i - 1]) - 1):
                        _list.append(triangle[i - 1][j] + triangle[i - 1]
                                     [j + 1])
                    _list.append(triangle[i - 1][j + 1])
                    triangle.append(_list)
                    i += 1
                    del _list

    return triangle
