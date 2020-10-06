#!/usr/bin/python3
"""
This module defines a class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class defines a Rectangle
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Computes the area of a rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Returns a string representation of the object
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
