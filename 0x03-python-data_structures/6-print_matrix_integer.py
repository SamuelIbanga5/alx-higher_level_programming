#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            if j != 2:
                print("{}".format(i[j]), end=" ")
            else:
                print("{}".format(i[j]), end="")
        print("\n", end="")
