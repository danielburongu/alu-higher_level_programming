#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    numbers = 1, 2, 3, 4, 5
    if my_list is None:
        return None
    else:
        for number in my_list[::-1]:
            print("{:d}".format(number))
