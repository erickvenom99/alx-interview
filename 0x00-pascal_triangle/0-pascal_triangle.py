#!/usr/bin/python3
"""Generates Pascal's Triangle
"""
from math import factorial


def pascal_triangle(n):
    """Generate Pascal's triangle with n rows.
    Args:
        n (int): Number of rows in the triangle.
    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
