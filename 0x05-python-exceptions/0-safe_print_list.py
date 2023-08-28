#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    val = 0
    try:
        for m in range(x):
        val = my_list[n]
        print("{}".format(val), end="")
            
    except IndexError:
            break
    print()
    return val
