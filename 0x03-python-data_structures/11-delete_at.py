#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    L = len(my_list)
    if idx not in range(L):
        return(my_list)
    else:
        my_list.remove(my_list[idx])
        return(my_list)
