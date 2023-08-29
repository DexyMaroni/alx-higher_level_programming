#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    try:
        for m in range(x):
        print(my_list[a], end="")
        a += 1

    except (IndexError):
        print("Out of range")

    finally:
        print()
    return a
