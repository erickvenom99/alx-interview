#!/usr/bin/python3
"""Pascal's Triangle Generator
"""
from math import factorial


def pascal_triangle(n):
    """Generate Pascal's triangle with n rows.
    Args:
        n (int): The number of rows in the triangle.
    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        triangle.append(row)

    return triangle
