#!/usr/bin/python3
for i in range(0, 100):
    if i < 99:
        if i < 10:
            i = '0' + str(i)
        print("{}".format(i), end=', ')
    else:
        print("{}".format(i))
