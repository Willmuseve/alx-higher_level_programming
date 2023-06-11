#!/usr/bin/python3
"""
A function that prints My name
"""


def say_my_name(first_name, last_name=""):
    """function that prints full names"""
    if type(first_name) != str or first_name == "":
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    """print(f"{My name is {first_name} {last_name}")"""
    print("My name is {} {}".format(first_name, last_name))
