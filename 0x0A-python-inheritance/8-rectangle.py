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

        self.__width = super().integer_validator('name', width)
        self.__height = super().integer_validator('name', height)
