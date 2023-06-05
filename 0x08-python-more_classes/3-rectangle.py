#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of rectangle.
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves width
        """
        return self.__width

    @property
    def height(self):
        """Retrieves height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates area of a rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter of a rectangle.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints the rectangle with the character #
        """
        rectangle = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")
        # remove blank line
        rectangle.pop()
        return "".join(rectangle)
