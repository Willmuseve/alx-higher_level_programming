#!/usr/bin/python3
"""Thus module defines a function that 
reads text
    """


def read_file(filename=""):
    """ Reads a text file and prints it  """

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
