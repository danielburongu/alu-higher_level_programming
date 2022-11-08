#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print("True")
    except:
        print("False")
