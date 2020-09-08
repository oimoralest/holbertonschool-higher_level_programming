#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        _max = my_list[-1]
        for i in my_list:
            if i > _max:
                _max = i
        return _max
    else:
        return None
