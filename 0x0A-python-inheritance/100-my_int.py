#!/usr/bin/python3
"""
This module defines a class MyInt
"""


class MyInt(int):
    """
    Defines MyInt
    """
    def __init__(self, value=0):
        """
        Initializes MyInt
        """
        self.__value = value

    def __eq__(self, value):
        """
        Truncates == operator
        """
        return not (self.__value == value)

    def __ne__(self, value):
        """
        Truncates != operator
        """
        return not (self.__value != value)
