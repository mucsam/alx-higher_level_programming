#!/usr/bin/python3
"""First Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances of Rectangle class
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the Rectangle's width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the Rectangle's height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of width
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Retrieves the Rectangle's x value"""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Retrieves the value of y
        """

        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Computes area of the rectangle"""

        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #
        """

        i = 0
        while i < self.__height:
            print("#" * self.__width)
            i += 1
