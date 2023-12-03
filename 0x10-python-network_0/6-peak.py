#!/usr/bin/python3

"""
Finfs a peak in an unsorted integer list
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(list): unsorted intefers lists
    Return:  the peak
    """

    if type(list_of_integers) != list:
        return

    if not list_of_integers:
        return None


    left = 0
    right = len(list_of_integers) - 1


    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
