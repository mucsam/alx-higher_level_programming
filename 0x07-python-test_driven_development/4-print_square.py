#!/usr/bin/python3
"""Documentation for a function that prints a square
with character #
"""


def print_square(size):
    """prints a square with the character #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
