#!/usr/bin/python3
""" a function that writes an Object to a text
file, using a JSON representation """

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a test file - json"""
    with open(filename, 'w') as o:
        return o.write(json.dumps(my_obj))
