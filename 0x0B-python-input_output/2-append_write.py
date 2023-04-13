#!/usr/bin/python3
"""This module defines a function that appends a file"""


def append_write(filename, text=""):
    """Append"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
