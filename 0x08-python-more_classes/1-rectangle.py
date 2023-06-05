#!/usr/bin/python3


"""Defining a class Rectangle"""


class Rectangle:
    """
    Class that is used to define properties of a
     rectangle.
    """

    def __init__(self, width=0, height=0):
        """Creates new instances of a Rectangle.
        """
        self.width = 0
        self.height = 0
        self.height = height
        self.width = width

    @property
    def width(self):
        """retries the width
        """
        return self.__width

    @property
    def height(self):
        """retrieves the height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Property setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
