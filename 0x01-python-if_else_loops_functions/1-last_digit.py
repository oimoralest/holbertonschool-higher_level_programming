#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
flag = 1
if number < 0:
        flag = -1
ld = int((number * flag) % 10)
if ld > 5:
        print(
            "Last digit of", number, "is", ld * flag, "and is greater than 5")
elif ld == 0:
        print(
            "Last digit of", number, "is", ld * flag, "and is 0")
else:
        print(
            "Last digit of", number, "is", ld * flag, "and is less than 6 and \
not 0")
