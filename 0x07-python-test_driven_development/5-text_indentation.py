#!/usr/bin/python3
"""
This module indents texts
"""


def text_indentation(text):
    """prints a text with 2 new lines after each; ".", "?", or ":"
    
    Arguments:
        text (str): The printed string
    
    Raise:
        TypeError: If not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == " ":
        c = c + 1

    while c < len(text):
        print(text[count], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c = c + 1
            while c < len(text) and text[c] == " ":
                c = c + 1
            continue
        c = c + 1
