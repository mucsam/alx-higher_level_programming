#!/usr/bin/python3

"""Printing a square"""


class Square:
    """A class that defines a class based on size"""

    def __init__(self, size=0):
        """Initializes an instance of the Square class"""

        self.__size = size

    @property
    def size(self):
        """Method to retrieve the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square"""

        return self.__size ** 2

    def my_print(self):
        """prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
