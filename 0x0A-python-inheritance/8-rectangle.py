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
