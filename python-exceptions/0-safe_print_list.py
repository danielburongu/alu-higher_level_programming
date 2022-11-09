#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    point_out = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            point_out += 1
    except:
        pass
    print()
    return point_out
