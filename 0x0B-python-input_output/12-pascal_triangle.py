#!/usr/bin/python3
"""defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Pascal's Triangle of size n
    """
    if n <= 0:
        return []

    t = [[1]]
    while len(t) != n:
        s = t[-1]
        tmp = [1]
        for i in range(len(s) - 1):
            tmp.append(s[i] + s[i + 1])
        tmp.append(1)
        t.append(tmp)
    return t
