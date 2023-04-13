#!/usr/bin/python3
"""This module defines a text-reading function"""

def read_file(filename=""):
    with open(filename, encoding="UTF-8") as o:
        print(o.read(), end="")

