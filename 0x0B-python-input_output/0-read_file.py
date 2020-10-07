#!/usr/bin/python3
"""
This modules defines read_file function
"""


def read_file(filename=""):
    """
    reads a text file (UTF-8) and prints it to sdtout
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
