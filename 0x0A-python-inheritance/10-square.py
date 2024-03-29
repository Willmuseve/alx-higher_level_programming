#!/usr/bin/python3
""" class Square that inherits from Rectangle (9-rectangle.py): """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area method """
        return self.__size ** 2
