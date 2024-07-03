#!/usr/bin/env python3

def summation_i_squared(n):
    """ Calcule the sum of squared of i """
    if type(n) is not int or n <= 0:
        sum = -1
    else:
        sum = (n * (n + 1) * (2 * n + 1)) / 6
    return int(sum)
