#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i, j = 0, 0
    new_list = []
    while i < list_length:
        try:
            j = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            j = 0
        except ZeroDivisionError:
            print("division by 0")
            j = 0
        except IndexError:
            print("out of range")
            j = 0
        finally:
            new_list.append(j)
            i += 1
    return new_list
