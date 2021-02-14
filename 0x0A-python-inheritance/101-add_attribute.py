#!/usr/bin/python3
"""
add attr
"""


def add_attribute(obj, atr, value):
    """
    add attr
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, atr, value)
    else:
        raise TypeError("can't add new attribute")
