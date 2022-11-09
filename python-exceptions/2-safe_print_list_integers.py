#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    point_in = 0
    for i in range(x):
        try:
            print('{:d}'.format(my_list[i]), end="")
            point_in += 1
        except (TypeError, ValueError):
            continue

    print()
    return point_in
