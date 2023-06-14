#!/usr/bin/python3
"""Reads a text file and prints it to std out"""


def read_file(filename=""):
    """ reading a text file of utf and prints to stdout"""
    with open(filename, encoding="utf-8") as o:
        print(o.read(), end="")
