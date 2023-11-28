#!/usr/bin/python3
"""A module for the write_file function
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the
    number of characters written
    """

    with open(filename, 'w', encoding='UTF8') as f:
        charactersWritten = f.write(text)
        return charactersWritten
