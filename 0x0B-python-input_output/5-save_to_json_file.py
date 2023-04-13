#!/usr/bin/python3
"""A module that defines function that writes  a JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
