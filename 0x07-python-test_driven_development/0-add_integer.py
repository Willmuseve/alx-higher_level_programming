#!/usr/bin/python3

"""
This module function adds two integers
"""

def add_integer(a, b=98):
    """Return a sum of two integers or floats as integers

    Arguments:
        a: first argument
        b: second argument

    Returns:
        Sum of the two arguments

    Raise:
        TypeError: If either of the arguments not an integer or a float
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    
    return (int(a) + int(b))
