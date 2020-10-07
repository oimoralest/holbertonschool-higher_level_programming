#!/usr/bin/python3
"""
This modules adds all arguments to a Python list, and then save them to a file
"""
import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if name == "main":
    try:
        my_list = load_from_json_file("add_item.json")
    except:
        my_list = []

    for i in sys.argv[1:]:
        my_list.append(i)
    save_to_json_file(my_list, "add_item.json")
