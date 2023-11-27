#!/usr/bin/python3
"""A module for MyList class that inherits from list
"""


class MyList(list):
    """MyList class that inherits from list
    """

    def print_sorted(self):
        """prints the list, sorted in ascending order"""

        print(sorted(self))
