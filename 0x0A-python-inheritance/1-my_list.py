#!/usr/bin/python3
"""
 class MyList that inherits from list
"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
