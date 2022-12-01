#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_length = len(argv)
    sum_of_arguments = 0
    for i in range(1, argv_length):
        if not argv[i].isalpha():
            num = int(argv[i])
            sum_of_arguments += num
    print("{}".format(sum_of_arguments))
