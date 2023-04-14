#!/usr/bin/python3
"""A function that returns a list of lists of integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):

    if n <= 0:
        return []

    s = [[1]]
    while len(s) != n:
        t = s[-1]
        tmp = [1]
        for i in range(len(t) - 1):
            tmp.append(t[i] + t[i + 1])
        tmp.append(1)
        s.append(tmp)
    return s
