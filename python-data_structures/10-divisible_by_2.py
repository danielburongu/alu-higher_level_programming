#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    z = []
    for i in my_list:
        if i % 2 == 0:
            z.append(True)
        else:
            z.append(False)
    return z
