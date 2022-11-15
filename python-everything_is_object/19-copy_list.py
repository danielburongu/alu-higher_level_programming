#!/usr/bin/python3
def copy_list(l):
    my_list = [1, 2, 3]
    print(my_list)
    new_list = copy_list(my_list)
    print(my_list)
    print(new_list)
    print(new_list == my_list)
    print(new_list is my_list)