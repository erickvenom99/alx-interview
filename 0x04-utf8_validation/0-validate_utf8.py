#!/usr/bin/python3
"""UTF-8 Validation module"""


def validUTF8(data):
    """
    Determines if a data set represents a valid UTF-8 encoding.
    Args:
        data: A list of integers representing bytes of data
    Returns:
        True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0
    i = 0

    while i < len(data):
        byte = data[i]

        if num_bytes == 0:
            if byte >> 7 == 0:
                num_bytes = 0
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

        i += 1

    return num_bytes == 0
