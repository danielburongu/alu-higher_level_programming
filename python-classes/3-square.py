#!/usr/bin/python3
"Create a square "


class Square:
    '''
    Create a square
        Has a private Instance att: size
    '''

    def __init__(self, size=0):
        ''' init size '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        square_area = self.__size ** 2
        return square_area
