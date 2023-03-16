#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_integers = set()
    for element in my_list:
        if isinstance(element, int) and element not in unique_integers:
            unique_integers.add(element)
    result = sum(unique_integers)

    return result
