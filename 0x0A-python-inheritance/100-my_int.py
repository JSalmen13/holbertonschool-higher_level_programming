#!/usr/bin/python3
"""
int subclass
"""


class MyInt(int):
    """
    int subclass
    """
    def __init__(self, value):
        """
        MyInt int
        """
        self.value = value

    def __eq__(self, obj):
        """
        equal int
        """
        return (obj != self.value)

    def __ne__(self, obj):
        """
        not equal int
        """
        return (obj == self.value)
