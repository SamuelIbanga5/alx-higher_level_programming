#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_length = len(argv)
    argument = ""
    if argv_length == 1:
        print("{} arguments.".format(0))
    elif argv_length > 2:
        print("{} arguments:".format(argv_length - 1))
        for i in range(1, argv_length):
            print("{}: {}".format(i, argv[i]))
    elif argv_length == 2:
        print("{} argument:".format(argv_length - 1))
        for i in range(1, argv_length):
            print("{}: {}".format(i, argv[i]))
