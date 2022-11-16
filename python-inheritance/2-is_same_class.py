#!/usr/bin/python3
''' Object is an exact instance of the specified class '''


def is_same_class(obj, a_class):
    '''The object is an instance of
    the class given
    Args:
        obj: The object to check
        a_class: The class to check
    '''
    return type(obj) is a_class
