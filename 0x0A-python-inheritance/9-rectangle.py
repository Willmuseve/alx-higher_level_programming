#!/usr/bin/python3
""" class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py) """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area"""
        return self.__width * self.__height

    def __str__(self):
        """ __str__ method """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
