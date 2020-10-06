#!/usr/bin/python3
"""
This modules define a class MyList that inherits from list
"""


class MyList(list):
    """
    This class is a subclass of list
    """
    def __init__(self):
        """
        This method initializes MyList
        """
        super().__init__

    def print_sorted(self):
        """
        This method print MyList sorted
        """
        print(sorted(self))
