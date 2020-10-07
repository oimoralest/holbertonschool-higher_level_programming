#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then save them to a file
"""


from sys import argv
save_to = __import__("7-save_to_json_file").save_to_json_file
load_from = __import__("8-load_from_json_file").load_from_json_file

try:
    _list = load_from("add_item.json")
except (FileExistsError, FileNotFoundError, ValueError):
    _list = []
for i in argv[1:]:
    _list.append(i)
save_to(_list, "add_item.json")
