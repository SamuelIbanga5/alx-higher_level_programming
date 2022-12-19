#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for index in range(x):
        try:
            print(my_list[index], end="")
        except IndexError:
            break
    print("\n", end="")
    if x <= len(my_list):
        return x
    else:
        return len(my_list)
