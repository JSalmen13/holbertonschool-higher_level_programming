#!/usr/bin/python3
"""
Inherit
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square"""
    def __init__(self, size):
        """
        init
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)

    def __str__(self):
        return("[Square] {}/{}".format(self.__size, self.__size))
