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

    @property
    def size(self):
        """Retrieves the size of the square"""

        return self.width

    @size.setter
    def size(self, value):
        """Sets the square size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes to the square"""

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""

        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
