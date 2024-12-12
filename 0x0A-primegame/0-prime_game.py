#!/usr/bn/python3
"""
MODULES DETERMINE THE WINNER IN A PRIME GAME
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
      x: The number of rounds.
      nums: An array of n, where n is the upper limit for each round.

    Returns:
      Player name, or None if no winner can be determined.
    """
    if not x or not nums:
        return None
    if x != len(nums):
        return None

    maria = 0
    ben = 0

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        total_primes = len(primes)

        if total_primes % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(k):
    """
    Finds all prime numbers up to n using the Sieve of Eratosthenes.

    Args:
        k: The upper limit for finding primes.

    Returns:
        A list of prime numbers up to n.
    """
    primes = [True] * (k + 1)
    primes[0] = primes[1] = False

    for p in range(2, int(k**0.5) + 1):
        if primes[p]:
            for i in range(p * p, k + 1, p):
                primes[i] = False

    prime_numbers = []
    for p in range(k + 1):
        if primes[p]:
            prime_numbers.append(p)

    return prime_numbers