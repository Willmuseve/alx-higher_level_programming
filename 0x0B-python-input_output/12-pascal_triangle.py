#!/usr/bin/python3
"""A function that returns a list of lists of integers representing the Pascal’s triangle of n"""

def pascal_triangle(n):
    """pascal triangle"""

    list = []

    for m in range(m):
        list.append([])
        list[m].append(1)
        for l in range(1, m):
            list[m].append(list[m - 1][l - 1] + list[m - 1][l])
        if(m != 0):
            list[m].append(1)

    return list
