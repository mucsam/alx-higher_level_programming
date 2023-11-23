#!/usr/bin/python3
"""A documentation for a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """Prints  first and last name

    Args:
        first_name: first name value
        last_name: last name value
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
