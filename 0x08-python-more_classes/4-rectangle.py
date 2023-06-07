#!/usr/bin/python3


""" Rectangle
Define the class Rectangle
    """


class Rectangle:
    """ Representation of a rect
    """


def __init__(self, width=0, height=0):
    """ Initializes the rectangle """

    self.width = width
    self.height = height


@property
def width(self):
    """ This returns the width of the rectangle """
    return self.__width


@width.setter
def width(self, value):
    """ Method that sets the width of the rectangle """
    if not type(int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value


@property
def height(self):
    """ Method use to return the height of the retangle """
    return self.__height


@height.setter
def height(self, value):
    """ Method is used to set the height of the rectangle """
    if not type(int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value


def area(self):
    """ Calculates the rectangle area """
    return self.width * self.height


def perimeter(self):
    """ Method to calculate the rectangle perimeter"""
    if self.__width == 0 or self.__height == 0:
        return 0
    return (self.width * 2) + (self.height * 2)


def __str__(self):
    """ Method to represent the rectangle with # """
    if self.width == 0 or self.height == 0:
        return ""
    return ((("#" * self.width) + "\n") * self.height)[:-1]


def __repr__(self):
    """ Extract the representation of the rectangle with repr """
    return "Rectangle({}, {})".format(self.width, self.height)
