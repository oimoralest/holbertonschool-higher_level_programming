#!/usr/bin/python3
"""This module creates a class Square"""


class Square:
    """Square class that represents a square

    Attributes:
        __size (int): size of the side of a square
    """
    def __init__(self, size=0):
        """ Initializes a square

        Args:
            size (int): size of the side of a square

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
