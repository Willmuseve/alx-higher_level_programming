#!/usr/bin/python3
"""Returns a list of available attributes and methods of an object."""


def lookup(obj):
    """returns list of dir()"""
    return([y for y in dir(obj)])
