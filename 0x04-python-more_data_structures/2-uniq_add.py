#!/usr/bin/python3
def uniq_add(my_list=[]):
    val = 0
    for i in set(my_list):
        val += i
    return val
