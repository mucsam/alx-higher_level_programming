#!/usr/bin/python3
"""A module for the BaseGeometry class
"""


class BaseGeometry:
    """A BaseGeometry class
    """

    def area(self):
        """Raises an Exception with the the message
        area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
