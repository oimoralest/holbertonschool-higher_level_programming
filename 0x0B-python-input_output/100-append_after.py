#!/usr/bin/python3
"""
This module defines append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file, after each line containing
    a specific string
    """
    if type(search_string) is str and search_string != "" \
       and type(new_string) is str:
        with open(filename, mode="r") as file:
            _list = file.readlines()
            for i in _list:
                if i.find(search_string) >= 0:
                    index = _list.index(i)
                    _list.insert(index + 1, new_string)
        with open(filename, mode="w") as file:
            file.writelines(_list)
