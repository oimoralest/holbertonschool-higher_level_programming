#!/usr/bin/python3
"""
This modules defines read_lines function
"""


def read_lines(filename="", nb_lines=0):
    """
    reads nb_line of a text file (UTF-8) and prints it to stdout
    """
    with open(filename, encoding="utf-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        else:
            i = 0
            while i < nb_lines:
                print(file.readline(), end="")
                i += 1
