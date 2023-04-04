#!/usr/bin/python3

"""This module defines a template for creating rectangle objects"""


class Rectangle:
    """This is a class that defines a rectangle
    Args:
        number_of_instances (int): Count for the number of instances
                                    available in the class
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes rectangle instance with a width and height
        Args:
            width (int): The breadth of a rectangle
            height (int): The height of a rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the ara of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle object in a pretty format"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]

            if i != self.__height - 1:
                rect.append("\n")

        return "".join(rect)

    def __repr__(self):
        """Returns a rectangle object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
