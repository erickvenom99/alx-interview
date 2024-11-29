#!/usr/bin/python3
"""
Module to determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Function determines the fewest number of coins needed to
    meet a given amount total.
    Args:
        coins: List of coin denominations
        total: The total amount of money
    Returns:
        The fewest number of coins needed to meet the total,
        or -1 if the total cannot be met by any combination of coins.
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    amount_left = total

    for coin in coins:
        while amount_left >= coin:
            amount_left -= coin
            count += 1

    if amount_left == 0:
        return count
    else:
        return -1
