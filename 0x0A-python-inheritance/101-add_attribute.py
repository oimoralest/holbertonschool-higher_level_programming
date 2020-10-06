#!/usr/bin/python3
"""
This module defines a function add_attribute
"""


def add_attribute(_object, name, value):
    """
    adds a new attribute to an object if it’s possible
    """
    if getattr(_object, '__dict__', 0) != 0:
        setattr(_object, name, value)
    else:
        raise TypeError("can't add new attribute")
