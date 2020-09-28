#!/usr/bin/python3
"""
This module defines a class called Rectangle
"""


class Rectangle():
    def __init__(self, width=0, height=0):
        """This class defines a representation of a rectangle

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for the witdth

        Returns:
            int: private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width

        Args:
            value (int): width of the rectangle

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than Zero
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height

        Returns:
            int: private instance attribute height
        """
        return self.__width

    @height.setter
    def height(self, value):
        """Setter for the height

        Args:
            value (int): height of the rectangle

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than Zero
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
