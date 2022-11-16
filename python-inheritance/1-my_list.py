#!/usr/bin/python3
'''This file inherits from List functions '''


class MyList(list):
    '''This Class inherits function list'''

    def print_sorted(self):
        '''Prints the list in a sorted manner  '''
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
