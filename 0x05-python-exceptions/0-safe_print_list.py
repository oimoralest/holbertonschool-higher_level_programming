#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count, i = 0, 0
    try:
        while i < x:
            print("{}".format(my_list[i]), end="")
            count += 1
            i += 1
    except IndexError:
        pass
    finally:
        print()
        return count
