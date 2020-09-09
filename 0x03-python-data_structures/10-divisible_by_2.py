#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    L = len(my_list)
    if L > 0:
        new = list(my_list)
        for K in range(L):
            if my_list[K] % 2 == 0:
                new[K] = True
            else:
                new[K] = False
    else:
        return(None)
    return(new)
