#!/usr/bin/python3
"""
This module defines write_file function
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file and returns the number of characters written
    """
    with open(filename, encoding="utf-8", mode="w") as file:
        return file.write(text)
