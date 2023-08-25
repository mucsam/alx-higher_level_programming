#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_count = len(argv)
    if arg_count == 1:
        print("0 arguments.")
    elif arg_count == 2:
        print("1 argument")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(arg_count - 1))
        a = 1
        while a < arg_count:
            print("{}: {}".format(a, argv[a]))
            a += 1
