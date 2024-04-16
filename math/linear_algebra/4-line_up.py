#!/usr/bin/env python3
""" Documented """


def add_arrays(arr1, arr2):
    """ Adds two arrays element-wise """
    shape1 = []
    shape2 = []
    arr1_copy = arr1
    arr2_copy = arr2
    if not arr1 or not arr2:
        return []
    while type(arr1) is list:
        shape1.append(len(arr1))
        arr1 = arr1[0]
    while type(arr2) is list:
        shape2.append(len(arr2))
        arr2 = arr2[0]
    if shape1 != shape2:
        return None
    new_array = []
    for i in range(len(arr1_copy)):
        new_array.append(arr1_copy[i] + arr2_copy[i])
    return new_array
