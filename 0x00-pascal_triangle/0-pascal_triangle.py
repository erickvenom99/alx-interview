#!/usr/bin/python
"""pascal Traiangle
"""
from math import factorial


def pascal_triangle(n):
    """print a pascal triangle"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        triangle.append(row)

    return triangle
