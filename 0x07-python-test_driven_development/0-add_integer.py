#!/usr/bin/python3
"""
This module defines a function add_integer


"""


def add_integer(a, b=98):
    """
    This function adds two numbers
    """
    if (type(a) is int or type(a) is float) and \
       (type(b) is int or type(b) is float):
        return int(a) + int(b)
    elif (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    else:
        raise TypeError("b must be an integer")
