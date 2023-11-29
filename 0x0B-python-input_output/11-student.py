#!/usr/bin/python3
"""module for Student class
"""


class Student:
    """Student class
    """

    def __init__(self, first_name, last_name, age):
        """Intializes instances of Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        """
        my_dict = {}
        all_dict = self.__dict__
        if attrs is None:
            return all_dict
        else:
            for key in attrs:
                if all_dict.get(key) is not None:
                    my_dict[key] = all_dict[key]
            return my_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Studen instance
        """

        for key, value in json.items():
            setattr(self, key, value)
