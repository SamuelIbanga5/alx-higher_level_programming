#!/usr/bin/python3
def _len(iterable):
    if hasattr(iterable, "__iter__"):
        count = 0
        for i in iterable:
            count += 1
        return count
    else:
        return

def safe_print_list(my_list=[], x=0):
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
        except IndexError:
            break
    print("")
    if x <= _len(my_list):
        return x
    else:
        return _len(my_list)
