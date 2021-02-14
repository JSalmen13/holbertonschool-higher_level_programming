#!/usr/bin/python3
"""
add new class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """
        class init
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        area of rectangle
        """
        a = self.__width * self.__height
        return(a)

    def __str__(self):
        """
        format string
        """
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
