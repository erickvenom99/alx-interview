#!/usr/bin/python3
"""
Generates pascal triangle
"""


def pascal_triangle(n):
    """Generate Pascal's triangle with n rows.
    Args:
        n (int): Number of rows in the triangle.
    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        rowNo = [1]
        for j in range(1, i):
            rowNo.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        rowNo.append(1)
        triangle.append(rowNo)
    return triangle
