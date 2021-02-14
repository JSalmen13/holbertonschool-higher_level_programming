#!/usr/bin/python3
"""
inherit
"""


def inherits_from(obj, a_class):
    """a function that returns True or false
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return(True)
    else:
        return(False)
