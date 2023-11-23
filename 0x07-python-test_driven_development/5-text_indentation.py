#!/usr/bin/python3
"""A documentation for text_indentation function"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
    ., ?, and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i == '.' or i == '?' or i == ':':
            print()
            print()
