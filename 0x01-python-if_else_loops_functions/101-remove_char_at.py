#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        copy = str[:n] + str[n + 1:]
    else:
        return str
    return copy
