#!/usr/bin/python3

"""
This module contains a script that reads stdin line by line
"""

import sys
from collections import defaultdict


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}


def print_read_lines(total_size, status_counts):
    """
    Print computed lines.

    Args:
        total_size (int): Total file size from processed lines.
        status_counts (dict): A dictionary of status codes and their counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] != 0:
            print(f"{code}: {status_counts[code]}")


def read_lines(lines):
    """
    Computes total file size and counts status codes.

    Args:
        lines (list): List of input lines (strings).

    Returns:
        tuple: Total file size and a dictionary of status code counts.
    """
    total_size = 0
    status_counts = defaultdict(int)

    for line in lines:
        parts = line.split()
        if len(parts) >= 7:
            try:
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size
                if status_code in status_codes:
                    status_counts[status_code] += 1
            except (ValueError, IndexError):
                pass
    return total_size, status_counts


try:
    lines = []
    for x, line in enumerate(sys.stdin, start=1):
        lines.append(line.strip())
        if x % 10 == 0:
            curr_total_size, curr_status_counts = read_lines(lines)
            print_read_lines(curr_total_size, curr_status_counts)
            lines = []
except KeyboardInterrupt:
    pass
finally:
    curr_total_size, curr_status_counts = read_lines(lines)
    print_read_lines(curr_total_size, curr_status_counts)
