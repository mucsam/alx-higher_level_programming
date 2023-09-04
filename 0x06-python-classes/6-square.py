#!/usr/bin/python3

"""Coordinates of a square"""


class Square:
    """A class that defines a class based on size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes an instance of the Square class"""

        self.__size = size
        self.__postion = position

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

    @property
    def position(self):
        """Retrieves the position"""

        return self.__position

    @position.setter
    def position(self, value):
        """set the position"""

        if (not isinstance(position, tuple)) or (len(position) != 2) or (not isinstance(position[0], int)) or (not isinstance(position[1], int)) or (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
