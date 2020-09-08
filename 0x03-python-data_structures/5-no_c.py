#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for i in my_list:
        if my_list.count('c'):
            for j in range(0, my_list.count('c')):
                my_list.remove('c')
        if my_list.count('C'):
            for j in range(0, my_list.count('C')):
                my_list.remove('C')
    new_string = ''
    return new_string.join(my_list)
