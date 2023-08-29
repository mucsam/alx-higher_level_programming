#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if column == len(matrix[row]) - 1:
                print("{:d}".format(matrix[row][column]))
            else:
                print("{:d}".format(matrix[row][column]), end=" ")
