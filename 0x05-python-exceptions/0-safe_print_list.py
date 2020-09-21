#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    var = 0
    try:
        for nb in range(x):
            print(end="{}".format(my_list[nb]))
            var = var + 1
    except(IndexError):
        pass
    print()
    return var
