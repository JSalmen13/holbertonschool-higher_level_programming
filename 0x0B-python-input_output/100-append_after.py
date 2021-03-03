#!/usr/bin/python3
"""
Append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """Append_after"""
    with open(filename, "r+", encoding="utf-8") as f:
        s = ""
        for line in f:
            s += line
            if search_string in line:
                s += new_string
        f.seek(0)
        f.write(s)
