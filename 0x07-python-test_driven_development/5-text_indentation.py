#!/usr/bin/python3
"""
This module defines a function text_identation


"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is str:
        for i in text:
            if i in [":", ".", "?"]:
                j = text.index(i)
                if (j + 1 < len(text)) and text[j + 1] == " ":
                    text = text[:j + 1] + "\n\n" + text[j + 3:]
                else:
                    text = text[:j + 1] + "\n\n" + text[j + 1:]
        text = text.strip(" ")
        print(text, end="")
    else:
        raise TypeError("text must be a string")
