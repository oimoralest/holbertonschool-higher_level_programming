#!/usr/bin/python3
"""
This module defines a a function inherits_from
"""


def inherits_from(obj, a_class):
    """
    This function checks if obj inherits from a_class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
