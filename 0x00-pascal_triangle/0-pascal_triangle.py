#!/usr/bin/python3

"""
Function that returns a list of lists of integers
The integers represents the Pascal’s triangle of a particular degree
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing a Pascal’s triangle of n
    """

    if n <= 0:
        return []

    ret_list = [[1]]
    if n == 1:
        return ret_list

    if n == 2:
        ret_list.append([1, 1])
        return ret_list

    base = [1, 1]
    ret_list.append([1, 1])
    for i in range(n - 2):
        new = []
        for i in range(len(base) - 1):
            left = base[i]
            right = base[i + 1]
            new.append(left + right)
        new = [1] + new + [1]
        base = new
        ret_list.append(new)

    return ret_list
