#!/usr/bin/python3

""" This module adds two integers """

def add_integer(a, b=98):
    
    """ Check that both inputs are integers or floats """
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")


    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    
    return a + b
