#!/usr/bin/python3

def safe_print_integer_err(value):
    i = isinstance(value, int)
    print("{:d}".format(value)) if is_integer else print("Exception: wrong type", file=sys.stderr)
    return i
