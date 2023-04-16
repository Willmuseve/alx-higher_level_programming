#!/usr/bin/python3
""" creating a function method that checks for a subclass"""


def is_same_class(obj, a_class):
    """  The method that checks for a subclass"""

    return (type(obj) == a_class)
