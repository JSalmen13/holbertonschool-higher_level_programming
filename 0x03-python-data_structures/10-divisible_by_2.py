def divisible_by_2(my_list=[]):
    new_list = []
    L = len(my_list)
    for x in range(L):
        if my_list[x] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
