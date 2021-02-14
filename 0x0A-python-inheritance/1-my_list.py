#!/usr/bin/python3
"""
add new class that inherist list
"""


class MyList(list):
    """
    a new class from list
    """
    def print_sorted(self):
        """
        print sorted list
        """
        print(sorted(self))

    def __str__(self):
        """
        returns the list
        """
        return (str(list(self)))
