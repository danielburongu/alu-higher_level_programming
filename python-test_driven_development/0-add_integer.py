#!/usr/bin/python3
"""
This module adds two integers and returns the addition of two numbers a and b.
Only accepts integers and floats else TypeError is raised
This module must be float or integer
"""


def add_integer(a, b=98):
    """
    add_integer: Check input if correct, cast both into ints and return sum
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    elif isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    return(int(a) + int(b))
