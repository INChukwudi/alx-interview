#!/usr/bin/python3

"""
Module holds the method that determines if a given data set
is a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Method that determines if a given data set is a valid
    UTF-8 encoding
    """
    continuation_bytes = 0
    for num in data:
        if continuation_bytes == 0:
            if (num >> 5) == 0b110:
                continuation_bytes = 1
            elif (num >> 4) == 0b1110:
                continuation_bytes = 2
            elif (num >> 3) == 0b11110:
                continuation_bytes = 3
            elif num >> 7:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            continuation_bytes -= 1
    return continuation_bytes == 0
