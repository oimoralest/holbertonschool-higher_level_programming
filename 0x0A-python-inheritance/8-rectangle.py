#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
This module defines a class Rectangle
"""


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
