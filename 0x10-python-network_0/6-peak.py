#!/usr/bin/python3
"""This script computes the peak of list of integers"""


def find_peak(list_of_integers):
    """Computes the peak"""
    mid = (len(list_of_integers) // 2) - 1 if len(list_of_integers) % 2 == 0 \
        else len(list_of_integers) // 2
    if len(list_of_integers) <= 2:
        return
    elif len(list_of_integers) == 3 and list_of_integers[mid - 1] <= \
        list_of_integers[mid] and list_of_integers[mid] >= \
            list_of_integers[mid + 1]:
        return list_of_integers[mid]
    else:
        return find_peak(list_of_integers[:mid]) or \
            find_peak(list_of_integers[mid:])

if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2, 1]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
