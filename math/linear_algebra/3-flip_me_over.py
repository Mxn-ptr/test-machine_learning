#!/usr/bin/env python3
""" Documented """


def matrix_transpose(matrix):
    """ Returns the transpose of a 2D matrix """
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose
