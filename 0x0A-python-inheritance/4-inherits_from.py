#!/usr/bin/python3
"""checks for an  instance of a given class"""


def inherits_from(obj, a_class):
    """will return true if is an instance of a class """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
