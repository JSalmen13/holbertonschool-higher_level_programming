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
        prints sorted list
        """
        return(print(sorted(self)))
