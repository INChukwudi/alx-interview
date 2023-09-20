#!/usr/bin/python3
"""
Making Chnage Module
"""


def makeChange(coins, total):
    """
    makechange method
        - Given a pile of coins of different values
          it determines the fewest number of coins needed to meet an amount

    Args:
    coins (list) - a list of available coins
    total (int) - the amount to be met

    Return:
        - number of coins needed to make change of the total
    """
    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if min_coins[i - coin] != float('inf'):
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
