#!/usr/bin/python3
""" function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """Appends a string of a text file and returns the number of 
    characters added"""
    with open(filename, 'a') as o:
        return o.write(text)
