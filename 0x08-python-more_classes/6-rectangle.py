#!/usr/bin/python3
"""
This module defines a class called Rectangle
"""


class Rectangle():
    """
    This class defines a representation of a rectang
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """This method initializes a rectangle

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return self.__height

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

    def area(self):
        """This method computes the area of the rectangle

        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """This method computes the perimeter of the rectangle

        Returns:
            int: the perimeter of the rectangle
        """
        perimeter = 0
        if self.__height != 0 and self.__width != 0:
            perimeter = 2 * self.__width + 2 * self.__height
        return perimeter

    def __str__(self):
        """This method return a string representation of the rectangle

        Returns:
            str: string representation of the rectangle
        """
        string = ""
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                string += "".join("#" for j in range(self.__width))
                string += "".join("\n")
        return string[:-1]

    def __repr__(self):
        """This method return a string representation of the class Rectangle

        Returns:
            str: string representation of the class
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when a instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
