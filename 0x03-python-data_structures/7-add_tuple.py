#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    new_lst = []
    new_i = 0
    new_j = 0
    if len(a) == 2 and len(b) == 2:
        pass
    else:
        if len(a) < 2:
            a.append(0)
        elif len(b) < 2:
            if len(b) == 0:
                b.append(0)
                b.append(0)
            else:
                b.append(0)
    for (i, j) in (a, b):
        new_i += i
        new_j += j
    new_lst.append(new_i)
    new_lst.append(new_j)
    return tuple(new_lst)
