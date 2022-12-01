#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for string in dir(hidden_4):
        if not string.startswith("__"):
            print("{:s}".format(string))
