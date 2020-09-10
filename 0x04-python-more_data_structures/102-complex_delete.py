#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    _list = []
    for key, value_ in a_dictionary.items():
        if value is value_:
            _list.append(key)
    for key in _list:
        del a_dictionary[key]
    return a_dictionary
