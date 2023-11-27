#!/usr/bin/python3
"""A module for the square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """Initializes instances of Square
        """

        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """computes the area of the square
        """

        return self.__size * self.__size

    def __str__(self):
        """string representation of the square
        """

        return "[Rectangle] {}/{}".format(self.__size, self.__size)
