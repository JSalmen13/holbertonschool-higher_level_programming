#!/usr/bin/python3
"""
add new func
"""


def is_kind_of_class(obj, a_class):
    """
    return boolean
    """
    if isinstance(obj, a_class) is True:
        return(True)
    else:
        return(False)
