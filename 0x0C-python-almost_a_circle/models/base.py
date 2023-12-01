#!/usr/bin/python3
"""Base model class
"""
import json


class Base:
    """Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instances of Base class
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
