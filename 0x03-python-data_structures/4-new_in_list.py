#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_of_list = my_list.copy()
    if idx < 0:
        return copy_of_list
    elif idx >= len(my_list):
        return copy_of_list
    else:
        copy_of_list[idx] = element
        return copy_of_list
