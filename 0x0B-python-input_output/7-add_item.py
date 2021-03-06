#!/usr/bin/python3
"""
Load, add, save
"""


import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"

    if os.path.isfile(filename) is not True:
        with open(filename, 'w') as f:
            my_list = []
            for i in range(1, len(sys.argv)):
                my_list.append(sys.argv[i])
            save_to_json_file(my_list, filename)
    else:
        if len(sys.argv) - 1 == 0:
            pass
        else:
            my_list = load_from_json_file(filename)
            for i in range(1, len(sys.argv)):
                my_list.append(sys.argv[i])
            save_to_json_file(my_list, filename)
