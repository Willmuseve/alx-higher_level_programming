#!/usr/bin/python3
""" a class BaseGeometry (based on 6-base_geometry.py). """


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        raises an Exception with the message area()
        is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validato
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
