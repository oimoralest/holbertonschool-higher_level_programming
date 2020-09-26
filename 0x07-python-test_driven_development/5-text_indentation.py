#!/usr/bin/python3
"""
This module defines a function text_identation


"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is str:
        _text = text.replace(".", ".\n\n").replace(":", ":\n\n")\
            .replace("?", "?\n\n")
        _text = _text.splitlines(True)
        for line in _text:
            print(line.strip(" "), end="")
    else:
        raise TypeError("text must be a string")
