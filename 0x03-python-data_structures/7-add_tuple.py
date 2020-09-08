#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        x, y = tuple_a[0] + tuple_b[0], tuple_b[1] + tuple_a[1]
    else:
        x = (0 if len(tuple_a) < 1 else tuple_a[0]) +\
            (0 if len(tuple_b) < 1 else tuple_b[0])
        y = (0 if len(tuple_a) < 2 else tuple_a[1]) +\
            (0 if len(tuple_b) < 2 else tuple_b[1])
    return x, y
