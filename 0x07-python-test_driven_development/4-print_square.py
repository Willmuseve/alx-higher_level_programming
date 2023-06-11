#!/usr/bin/python3
""" A  function that prints a square with the character #."""


def print_square(size):
    """A function that prints a square with the character #."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for l in range(size):
        for k in range(size):
            print("#", end="")
        print()
