#!/usr/bin/python3
"""A programme that Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):

    s = len(list_of_integers)
    n= size
    m = size // 2

    if s == 0:
        return None

    while True:
        n = n // 2
        if (m < s - 1 and
                list_of_integers[m] < list_of_integers[m + 1]):
            if n // 2 == 0:
                n = 2
            m = m + n // 2
        elif n > 0 and list_of_integers[m] < list_of_integers[m - 1]:
            if n // 2 == 0:
                n = 2
            m = m - n // 2
        else:
            return list_of_integers[m]
