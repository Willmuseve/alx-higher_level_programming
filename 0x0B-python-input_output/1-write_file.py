#!/usr/bin/python3
"""A This module defines a function that writes a file"""


def write_file(filename="", text=""):
    """number of characters """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
