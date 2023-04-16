#!/usr/bin/python3
""" empty class"""


class BaseGeometry:
    """class method"""

    def area(self):
        """calculates the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ inherits  parent class"""

    def __init__(self, width, height):
        """initializes rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
