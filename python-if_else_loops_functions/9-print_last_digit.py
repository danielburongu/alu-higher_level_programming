#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 123 > ord(char) > 96:
            char = chr(ord(char) - 32)
        print('{}'.format(char), end="")
    print('')
