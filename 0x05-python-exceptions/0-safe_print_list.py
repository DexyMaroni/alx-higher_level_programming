#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for c in range(x):
        try:
            print(my_list[c], end="")
            a += 1
        except IndexError:
            break
    print()
    return a
