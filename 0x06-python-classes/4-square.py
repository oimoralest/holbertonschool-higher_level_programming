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

        Returns: None
        """
        self.size = size

    @property
    def size(self):
        """ Getter of __size

        Returns:
            Value of the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter of __size

        Args:
            value (int): size of the side of a square

        Return:
            None

        Raises:
            TypeError: if type(value) is not int
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Computes the area of the square

        Returns:
            the are of the square
        """
        return self.__size ** 2
