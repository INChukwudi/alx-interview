#!/usr/bin/python3
"""
0-island_perimeter.py module
"""


def island_perimeter(grid):
    """
    island_perimeter function

    Args:
    grid - a list of lists of integers

    Return:
    value - int
    """
    if not isinstance(grid, list):
        print("Grid must be a list")
        return

    if not all(isinstance(row, list) for row in grid):
        print("Grid must be a list of lists")
        return

    if len(grid) < 1 or len(grid) > 100:
        print("Grid height must be between 1 and 100")
        return

    if len(grid[0]) < 1 or len(grid[0]) > 100:
        print("Grid width must be between 1 and 100")
        return

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
