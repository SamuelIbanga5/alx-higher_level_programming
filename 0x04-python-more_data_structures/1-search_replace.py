#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if my_list[i] == search:
            del new_list[i]
            new_list.insert(i, replace)
    return new_list
