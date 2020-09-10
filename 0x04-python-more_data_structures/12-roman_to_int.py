#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) == str:
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(roman_string)):
            if i > 0 and num[roman_string[i]] > num[roman_string[i - 1]]:
                res += (num[roman_string[i]] - 2 * num[roman_string[i - 1]])
            else:
                res += num[roman_string[i]]
        return res
    return 0
