#!/usr/bin/python3
"""
This module defines a Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    This class defines a Rectanlge
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        Rectangle.raise_("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        Rectangle.raise_("height", value)
        self.__height = value

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x
        """
        Rectangle.raise_("x", value)
        self.__x = value

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y
        """
        Rectangle.raise_("y", value)
        self.__y = value

    @staticmethod
    def raise_(name, value):
        """
        Handle the raise exceptions
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """
        Computes the Rectangle area
        """
        return self.width * self.height

    def display(self):
        """
        Display a Rectangle with the character #
        """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of Rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Updates the Rectangle
        """
        keys = ['id', 'width', 'height', 'x', 'y']
        if kwargs and len(args) == 0:
            for key, value in kwargs.items():
                if key in keys:
                    setattr(self, key, value)
        elif args is not None:
            for key, value in zip(keys, args):
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dict representation of Rectangle
        """
        keys = ['id', 'width', 'height', 'x', 'y']
        dict_ = {}
        for key in keys:
            dict_[key] = getattr(self, key)
        return dict_
