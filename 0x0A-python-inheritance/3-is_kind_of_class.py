#!/usr/bin/python3
""" A function that returns a class or inherit from a given class """


def is_kind_of_class(obj, a_class):
    """
    Return true if the object is an instance of a class or if
    the object is an instance of a class that inherited from, the
    specified class ; otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
