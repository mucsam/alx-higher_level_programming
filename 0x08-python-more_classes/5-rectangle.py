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
            raise ValueError("width must be >= 0")
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

    def area(self):
        """Returns the rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if (self.__height == 0) or (self.__width == 0):
            return 0
        perimeter = (self.__height + self.__width) * 2
        return perimeter

    def __str__(self):
        """Returns the string representation of the rectangle objects"""

        if (self.__height == 0) or (self.__width == 0):
            return ""
        row = "#" * self.__width
        result = (row + "\n") * (self.__height - 1) + row
        return result

    def __repr__(self):
        """Returns a formal string representation of objects"""

        return "Rectangle(" + str(self.__width) + "," + str(
                self.__height) + ")"

    def __del__(self):
        """Deleting the Rectangle instances"""

        print("Bye rectangle...")
