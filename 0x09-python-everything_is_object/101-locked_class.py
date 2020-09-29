#!/usr/bin/python3
"""
This modules defines a class called LockedClass
"""


class LockedClass():
    """
    This class prevents the user from dinamically creating new instances
    attributes
    """
    __slots__ = ["first_name"]
