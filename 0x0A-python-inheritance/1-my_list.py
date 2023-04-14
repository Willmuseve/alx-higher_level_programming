#!/usr/bin/python3
"""
 class MyList that inherits from list
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initialization"""
        super().__init__()

    def print_sorted(self):
        """prints list"""
        print(sorted(self))
