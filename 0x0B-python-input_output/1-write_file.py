#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8) and returns the
number of characters written"""


def write_file(filename="", text=""):
    """Writing a string to a text file"""
    with open(filename, "y", encoding="utf-8") as o:
        return o.write(text)
