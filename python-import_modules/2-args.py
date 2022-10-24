#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_of_args = len(argv) - 1
    if num_of_args > 0:
        if num_of_args == 1:
            print("{} argument:".format(num_of_args))
        else:
            print("{} arguments:".format(num_of_args))
        values = 1
        for arg in argv[1:]:
            print("{}: {}".format(values, arg))
            values += 1
    else:
        print("{} arguments.".format(num_of_args))
