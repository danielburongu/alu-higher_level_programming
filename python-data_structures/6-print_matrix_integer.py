#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not row:
            print()
        else:
            for num in row:
                if num == row[-1]:
                    print('{:d}'.format(num))
                else:
                    print('{:d}'.format(num), end=" ")
