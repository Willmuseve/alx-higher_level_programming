#!/usr/bin/python3
""" Defined class """


class LockedClass:
    """
    does not allow user to use dynamic libraries
    """
    __slots__ = ['first_name']
