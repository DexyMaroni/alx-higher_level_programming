#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        a = 0
        for m in range(x):
        print(my_list[m], end="")
        a += 1

    except IndexError:
        pass

    except:
        pass


    print()
    return a
