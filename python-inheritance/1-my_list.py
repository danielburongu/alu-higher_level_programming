#!/usr/bin/python3
'''This file inherits from List functions '''


class MyList(list):
    '''This Class Inherits Function List'''

    def print_sorted(self):
        '''Prints the list In a soRted Manner  '''
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
