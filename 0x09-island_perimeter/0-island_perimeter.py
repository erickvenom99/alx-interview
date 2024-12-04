#!/usr/bin/python3
"""
Module returns a grid
"""


def island_perimeter(grid):
    """
    This program returns the perimeter of island
    describe in the grid
    Args:
      grid (list of list of int): represent island map
    Returns:
      int : island perimeter

    """
    row_length = len(grid)
    col_length = len(grid[0])

    perimeter = 0
    connections = 0
    for x in range(0, row_length):
        for y in range(0, col_length):
            if grid[x][y] == 1:
                perimeter += 4

                if x != 0 and grid[x - 1][y] == 1:
                    connections += 1
                if y != 0 and grid[x][y - 1] == 1:
                    connections += 1

    return perimeter - (connections * 2)
