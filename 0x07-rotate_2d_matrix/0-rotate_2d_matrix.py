!/usr/bin/python3

"""
Rotate 2D matrix module
"""


def rotate_2d_matrix(matrix):
    """
     Rotates a 2D matrix by 90 degrees

    Args:
        - Matrix: 2D matrix to rotate

    Returns:
        - 2D Matrix rotated by 90 degrees
    """
    n = len(matrix)

    for k in range(n):
        for j in range(k+1, n):
            matrix[k][j], matrix[j][k] = matrix[j][k], matrix[k][j]

    for k in range(n):
        matrix[k].reverse()
