#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        result = map(lambda x: x * x, i)
        new_matrix.append(list(result))
    return new_matrix
