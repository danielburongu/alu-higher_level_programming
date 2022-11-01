#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_of_args = len(argv) - 1
    if num_of_args == 0:
        print(0)
    else:
        sum = 0
        for arg in argv[1:]:
            sum += int(arg)

        print(sum)
