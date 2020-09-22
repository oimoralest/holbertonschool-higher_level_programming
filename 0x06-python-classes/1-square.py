#!/usr/bin/python3
"""This module creates a class Square"""


class Square:
    """Square class that represents a square

    Attributes:
        __size (int): size of the side of a square
    """
    def __init__(self, size):
        """ Initializes a square

        Args:
            size (int): size of the side of a square

        Returns: None
        """
        self.__size = size
