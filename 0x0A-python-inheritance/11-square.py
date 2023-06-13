#!/usr/bin/python3
""" a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py) """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area method """
        return self.__size ** 2

    def __str__(self):
        """ __str__ method """
        return "[Square] {}/{}".format(self.__size, self.__size)
