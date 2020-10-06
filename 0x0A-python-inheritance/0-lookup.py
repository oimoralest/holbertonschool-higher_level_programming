#!/usr/bin/python3
"""
This modules defines a lookup function
"""


def lookup(obj):
    """
    This function returns the list of available attributes and methods of an
    object
    """
    return dir(obj)
