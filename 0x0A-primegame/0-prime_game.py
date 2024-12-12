#!/usr/bin/python3
""" Prime Game module """


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
      x: The number of rounds.
      nums: An array of n for each round.

    Returns:
      The name of the player with the most wins, or None.
    """
    if (type(nums) is not list or not all([type(n) is int for n in nums]) or
            not all([n > -1 for n in nums])):
        return None

    if type(x) is not int or x != len(nums):
        return None

    maria = 0
    ben = 0

    for n in nums:
        prime_count = sum(1 for i in range(2, n+1) if find_prime(i))
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None


def find_prime(num):
    """
    Determin if a number is prime.

    Args:
    - num (int): The number to check.

    Returns:
    - bool: True if the number is prime otherwise False..
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
