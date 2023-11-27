#!/usr/bin/python3
"""A module for the class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes instances of Rectangle
        """

        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """computes the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """string representation of the rectangle
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
