#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return replace_in_list
    elif idx >= len(my_list):
        return replace_in_list
    else:
        my_list[idx] = element
        return my_list
