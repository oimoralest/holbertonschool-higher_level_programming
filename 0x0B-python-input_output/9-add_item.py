#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    filename = 'add_item.json'
    try:
        _list = load_from_json_file(filename)
    except:
        _list = []
    for arg in argv[1:]:
        _list.append(arg)
    save_to_json_file(_list, filename)
