#!/usr/bin/python3
"""A module for the load_from_json_file function
"""

import json


def load_from_json_file(filename):
    """Creates an Object from a "JSON file"
    """

    with open(filename, 'r', encoding='UTF8') as f:
        load(filename)
