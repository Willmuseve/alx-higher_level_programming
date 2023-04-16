#!/usr/bin/python3
"""empty class"""


class BaseGeometry:
    """class with  calculation method"""

    def area(self):
        """Method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
