#!/usr/bin/python3
"""A function that inserts a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file,
    after each line containing a specific string """
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            if search_string in line:
                f.write(line + new_string)
            else:
                f.write(line)
