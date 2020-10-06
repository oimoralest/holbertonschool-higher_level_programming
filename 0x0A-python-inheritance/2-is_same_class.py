#!/usr/bin/python3
"""
This module defines a function is_same_class
"""


def is_same_class(obj, a_class):
    """
    This function checks if obj is an instance of a_class
    """
    return type(obj) == a_class
