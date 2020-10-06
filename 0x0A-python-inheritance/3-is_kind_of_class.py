#!/usr/bin/python3
"""
This modules defines a function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    This function checks if obj is subclass or instance of a_class
    """
    return issubclass(type(obj), a_class)
