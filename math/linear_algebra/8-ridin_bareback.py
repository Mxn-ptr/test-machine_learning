#!/usr/bin/env python3
""" Documented """


def mat_mul(mat1, mat2):
    """ Performs matrix multiplication """
    if len(mat1[0]) != len(mat2):
        return None
    mult = []
    for i in range(len(mat1)):
        mult.append([])
        for j in range(len(mat2[0])):
            result = 0
            for k in range(len(mat2)):
                result += mat1[i][k] * mat2[k][j]
            mult[i].append(result)
    return mult
