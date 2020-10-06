#!/usr/bin/python3
"""
This module defines a class BaseGeometry
"""


class BaseGeometry:
    """
    This class defines BaseGeometry
    """
    def integer_validator(self, name, value):
        """
        This function validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """
        Not implemented
        """
        raise Exception("area() is not implemented")
