#!/usr/bin/python3
""" 
 a script that adds all arguments to a Python list, and then save them to a file

"""

from sys import argv

load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

try:
    json_file = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    json_file = []

for i in argv[1:]:
    json_file.append(i)

save_file(json_file, 'add_item.json')
