#!/usr/bin/python3
"""A function that adds 2 integers"""


def add_integer(a, b=98):
    """ Adds 2 integers
    
    Args:
        a: first parameter
        b: second parameter

    Returns:
            The sum of a and b
    """

    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b
