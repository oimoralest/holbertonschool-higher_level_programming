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

    def to_json(self):
        """
        retrieves a dictionary representation of a Student
        """
        return self.__dict__
