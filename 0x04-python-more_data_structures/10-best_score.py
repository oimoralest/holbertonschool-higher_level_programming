#!/usr/bin/python3
def best_score(a_dictionary):
    _max = None
    if a_dictionary:
        _max = max(a_dictionary, key=a_dictionary.get)
    return _max
