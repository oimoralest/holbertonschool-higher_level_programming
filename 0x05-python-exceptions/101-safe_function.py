#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
        result = None
    finally:
        return result
