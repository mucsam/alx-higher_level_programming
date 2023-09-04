#!/usr/bin/python3

"""Size validation"""


class Square:
    """A class that defines a class based on size"""

    def __init__(self, size=0):
        """Initializes an instance of the Square class"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
