#!/usr/bin/python3
"""The N queens puzzle module"""
from sys import argv

N = argv[1]
if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if not isinstance(N, int):
    print("N must be a number")
    exit(1)
elif N < 4:
    print("N must be at least 4")
    exit(1)
