#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for a in range(x):
        try:
            c = my_list[a]
            print("{}".format(c), end= "")
            a += 1

        except IndexError:
            break
    print()
    return (0)
