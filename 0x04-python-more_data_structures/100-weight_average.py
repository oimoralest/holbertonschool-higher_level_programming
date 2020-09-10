#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    if my_list:
        weigth = 0
        for i, j in my_list:
            result += (i * j)
            weigth += j
        result /= weigth
    return result
