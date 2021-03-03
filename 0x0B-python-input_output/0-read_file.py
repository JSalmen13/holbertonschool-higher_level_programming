#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """Read file"""
    with open(filename, 'r') as f:
        read_file = f.read()
        print(read_file, end='')
