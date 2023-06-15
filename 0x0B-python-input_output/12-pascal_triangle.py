#!/usr/bin/python3
"""A function that returns a list of lists of integers
representing the Pascal’s triangle of n """


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        t = triangle[-1]
        p = [1]
        for i in range(len(t) - 1):
            p.append(t[i] + t[i + 1])
        p.append(1)
        triangle.append(p)
    return triangle
