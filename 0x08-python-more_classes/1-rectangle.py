#!/usr/bin/python3
"""A rectangle class module"""


class Rectangle:
    """A class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes class Rectangle's objects"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the value of the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the Rectangle's height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the rectangle's height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
