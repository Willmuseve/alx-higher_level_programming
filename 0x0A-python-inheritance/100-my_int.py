#!/usr/bin/python3
"""has class MyInt that inherits from int"""


class MyInt(int):
    """Invert == and !="""

    def __eq__(self, value):
        """Override == with !="""
        return self.real != value

    def __ne__(self, value):
        """Override !=  with =="""
        return self.real == value
