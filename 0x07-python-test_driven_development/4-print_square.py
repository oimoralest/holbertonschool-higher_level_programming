#!/usr/bin/python3
"""
This module defines a function print_square


"""


def print_square(size):
    """
    prints a square with the character #
    """
    if type(size) is int:
        if size >= 0:
            for i in range(size):
                print("#" * size)
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
