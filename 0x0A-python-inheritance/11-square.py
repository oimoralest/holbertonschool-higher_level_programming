#!/usr/bin/python3
"""
This module defines a class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class defines a Square
    """
    def __init__(self, size):
        """
        Initializes a Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of a Square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the object
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
