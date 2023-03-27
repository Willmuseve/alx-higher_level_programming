#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (TypeError, ValueError) as e:
        print("Exception in function '{}': {}: {}".format(fct.__name__, type(e).__name__, e), file=sys.stderr)
        return None

