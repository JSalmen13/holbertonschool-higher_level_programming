#!/usr/bin/python3
"""size
"""


class Square:
    """square size
    """
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer") 
        else:
            self.__size = size
