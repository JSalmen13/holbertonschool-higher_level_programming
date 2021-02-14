#!/usr/bin/python3
"""
add new lass
"""


class BaseGeometry:
    """
    Class
    """
    def area(self):
        """aaa"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """aa"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
