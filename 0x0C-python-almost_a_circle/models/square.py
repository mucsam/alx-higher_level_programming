#!/usr/bin/python3
"""Module for the square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instances of the square class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of the square class"""

        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
