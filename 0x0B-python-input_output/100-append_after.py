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
        with open(filename, mode="r", encoding="utf-8") as file:
            _list = []
            for line in file:
                _list.append(line)
                if search_string in line:
                    _list.append(new_string)
        with open(filename, mode="w", encoding="utf-8") as file:
            file.writelines(_list)
