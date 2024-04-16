#!/usr/bin/env python3
""" Documented """


def add_matrices2D(mat1, mat2):
    """ Adds two matrics element-wise """
    if len(mat1) != len(mat2):
        return None
    if len(mat1[0]) != len(mat2[0]):
        return None
    new_array = []
    for i in range(len(mat1)):
        new_array.append([])
        for j in range(len(mat1[0])):
            new_array[i].append(mat1[i][j] + mat2[i][j])
    return new_array
