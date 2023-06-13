#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """inherits here"""

    def __eq__(self, value):
        """=="""
        return self.real != value

    def __ne__(self, value):
        """!="""
        return self.real == value
