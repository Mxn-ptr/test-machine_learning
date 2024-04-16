#!/usr/bin/env python3
""" Documented """


def cat_matrices2D(mat1, mat2, axis=0):
    """ Concatenate two matrices along a specific axis """
    new_matrix = []
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        for i in mat1:
            new_matrix.append(i.copy())
        for i in mat2:
            new_matrix.append(i.copy())
    else:
        if len(mat1) != len(mat2):
            return None
        for i in range(len(mat1)):
            new_matrix.append(mat1[i].copy() + mat2[i].copy())
    return new_matrix
