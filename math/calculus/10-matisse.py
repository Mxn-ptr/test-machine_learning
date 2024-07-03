#!/usr/bin/env python3
""" Module """


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial

    args:
        - poly: list of coefficients representing a polynomial

    Return: new list of coefficients representing
        the derivative of the polynomial
    """
    if type(poly) is not list or len(poly) == 0:
        return None
    if len(poly) == 1 and poly[0] == 0:
        return [0]
    result = []
    for index, element in enumerate(poly):
        if index != 0:
            result.append(index * element)
    return result
