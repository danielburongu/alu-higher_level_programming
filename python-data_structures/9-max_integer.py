#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        if len(my_list) == 1:
            return my_list[0]
        else:
            be1 = my_list[0]
            be2 = max_integer(my_list[1:])

            if be1 > be2:
                return be1
            else:
                return be2
