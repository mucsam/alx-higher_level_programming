#!/usr/bin/python3
"""Lookup module"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""

    return list(obj.__dict__)
