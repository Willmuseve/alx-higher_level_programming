#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        print("Exception: value is not an integer", file=sys.stderr)
        return False
