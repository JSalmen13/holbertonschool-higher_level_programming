#!/usr/bin/python3
"""
Write file
"""


def write_file(filename="", text=""):
    """write file"""
    with open(filename, 'w') as f:
        write_file = f.write(text)
        return(write_file)
