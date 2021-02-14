#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Inherit
"""


class Square(Rectangle):
    """square"""
    def __init__(self, size):
        """
        init
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)
