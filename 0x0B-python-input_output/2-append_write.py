#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """appends a string to a file"""
    with open(filename, 'a') as f:
        append_file = f.write(text)
        return(append_file)
