#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then save them to a file
"""
from sys import argv
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

file = "add_item.json"
try:
    _list = load_from_json_file(file)
except (FileExistsError, FileNotFoundError, ValueError):
    _list = []
for i in argv[1:]:
    _list.append(i)
save_to_json_file(_list, file)
