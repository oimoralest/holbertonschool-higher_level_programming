#!/usr/bin/python3
"""
This module defines a class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        Initializes a Square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Computes the area of a Square
        """
        return self.__size * self.__size
