#!/usr/bin/python3
""" 
 a script that adds all arguments to a Python list, and then save them to a file

"""
import sys


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file
args = sys.argv[1:]
json_l = "add_item.json"
try:
    my_list = load(json_l)
except FileNotFoundError:
    save(args, json_l)
else:
    my_list.extend(args)
    save(my_list, json_l)
