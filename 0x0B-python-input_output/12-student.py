#!/usr/bin/python3
"""
This module defines a Student class
"""


class Student:
    """
    Defines a Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student
        """
        _dic = {}
        if type(attrs) is list:
            for element in attrs:
                if type(element) is str and element in self.__dict__.keys():
                    _dic[element] = self.__dict__[element]
            return _dic
        else:
            return self.__dict__
