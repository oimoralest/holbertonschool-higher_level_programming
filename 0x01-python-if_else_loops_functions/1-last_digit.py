#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
flag = 1
if number < 0:
        flag = -1
        number *= -1
if (number % 10) > 5:
        print("The last digit of", number * flag, "is", number % 10, "and is \
greater than 5")
elif (number % 10) == 0:
        print("The last digit of", number * flag, "is", number % 10, "and is \
0")
else:
        print("The last digit of", number * flag, "is", number % 10, "and is \
less than 6 and not 0")
