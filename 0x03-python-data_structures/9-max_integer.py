#!/usr/bin/python3
def max_integer(my_list=[]):
    L = len(my_list)
    if not L:
        return None
    big = my_list[0]
    for x in range(L):
        if my_list[x] > big:
            big = my_list[x]
    return big