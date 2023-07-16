#!/usr/bin/python3

"""
FIle contains the minOperations method
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations needed

    Args:
    n (int) - the number of characters needed

    Return:
    value (int) - number of operations needed
    """
    if n == 1:
        return 0

    max_ops = n + 1
    min_ops = [max_ops] * (n + 1)

    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                factor_1 = j
                factor_2 = i // j
                min_ops[i] = min(min_ops[i], min_ops[factor_1] + factor_2)
                min_ops[i] = min(min_ops[i], min_ops[factor_2] + factor_1)

        if min_ops[i] == max_ops:
            min_ops[i] = i

    if min_ops[n] != max_ops:
        return min_ops[n]
    else:
        return 0
