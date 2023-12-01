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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            with open(filename, 'w', encoding="utf8") as f:
                f.write("[]")
        else:
            obj_dicts = [obj.to_dictionary() for obj in list_objs]
            with open(filename, 'w', encoding="utf8") as f:
                f.write(cls.to_json_string(obj_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
