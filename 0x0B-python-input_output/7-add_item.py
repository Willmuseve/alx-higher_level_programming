#!/usr/bin/python3
""" a script that adds all arguments to a Python list,
and then save them to a file """
from sys import argv


old_file = __import__('6-load_from_json_file').load_from_json_file
new_file = __import__('5-save_to_json_file').save_to_json_file

try:
    json_list = old_file('add_item.json')
except (ValueError, FileNotFoundError):
    json_list = []

for item in argv[1:]:
    json_list.append(item)

new_file(json_list, 'add_item.json')
