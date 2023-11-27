#!/usr/bin/python3
"""A module for the is_samee_class function
"""


def is_same_class(obj, a_class):
    """A function that returns true if the object is
    exactly an instance of the specified class;
    otherwise returns fals
    """

    if type(obj) is a_class:
        return True
    else:
        return False
