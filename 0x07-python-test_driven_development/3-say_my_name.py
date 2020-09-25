#!/usr/bin/python3
"""
This module defines a function say_my_name


"""


def say_my_name(first_name, last_name=""):
    """
    function that prints My name is <first name> <last name>
    """
    if type(first_name) is str and type(last_name) is str:
        print("My name is {} {}".format(first_name, last_name))
    elif type(first_name) is not str:
        raise TypeError("first_name must be a string")
    else:
        raise TypeError("last_name must be a string")
