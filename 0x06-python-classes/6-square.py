#!/usr/bin/python3
"""This module creates a class Square"""


class Square:
    """Square class that represents a square

    Attributes:
        __size (int): size of the side of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a square

        Args:
            size (int): size of the side of a square
            position (tuple): position of the square

        Returns: None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Getter for __position

        Return:
            the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for __position

        Args:
            value (tuple): position of the square

        Return:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Computes the area of the square

        Returns:
            the are of the square
        """
        return self.__size ** 2

    def my_print(self):
        """ Draws the square with # representation and position

        Return:
            None
        """
        if self.__size == 0:
            print()
            return
        if self.__position:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            print("".join(" " for j in range(self.__position[0])), end="")
            print("".join("#" for j in range(self.__size)))
