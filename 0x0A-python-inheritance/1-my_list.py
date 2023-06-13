#!/usr/bin/python3
class MyList(list):
"""defines class MyList that inherits from list and has a public method print_sorted()"""


    def print_sorted(self):
        print(sorted(self))
