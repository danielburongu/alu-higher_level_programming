#!/usr/bin/python3
'''Write a function that returns the dictionary description'''


def class_to_json(obj):
    '''Returns The dictionary Description with Simple data Structure'''
    return obj.__dict__
