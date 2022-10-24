#!/usr/bin/python3
for i in range(0, 10):
    for t in range(i + 1, 10):
        if i == 8 and t == 9:
            print("{}{}".format(i, t))
            break
        print("{}{}".format(i, t), end=", ")