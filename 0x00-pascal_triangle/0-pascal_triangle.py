#!/usr/bin/python3
"""
returns a list of lists of numbers
representing the pascal triangle
"""


def pascal_triangle(n):
    """Creates a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    res = []
    if n > 0:
        for x in range(1, n + 1):
            level = []
            C = 1
            for y in range(1, x + 1):
                level.append(C)
                C = C * (x - y) // y
            res.append(level)
    return res
