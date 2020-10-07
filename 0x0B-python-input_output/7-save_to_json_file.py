#!/usr/bin/python3
"""
This module defines save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
