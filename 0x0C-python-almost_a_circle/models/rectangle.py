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

        self.__width = value

    @property
    def height(self):
        """Retrieves the Rectangle's height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of width
        """

        self.__height = value

    @property
    def x(self):
        """Retrieves the Rectangle's x value"""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x
        """

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

        self.__y = value
