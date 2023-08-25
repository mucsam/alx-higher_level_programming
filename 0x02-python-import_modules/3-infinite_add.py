#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv) - 1
    sum = 0
    a = 1
    while a <= ac:
        sum += int(argv[a])
        a += 1
    print(sum)
