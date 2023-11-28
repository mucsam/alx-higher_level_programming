#!/usr/bin/python3
"""A module for the append_write function
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    and returns the number of characters added
    """

    with open(filename, 'a', encoding='UTF8') as f:
        AddedCharacters = f.write(text)
        return AddedCharacters
