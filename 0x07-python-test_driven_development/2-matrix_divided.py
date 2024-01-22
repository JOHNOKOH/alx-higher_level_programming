#!/usr/bin/python3
# 2-matrix_divided.py
"""A matrix division function is defined."""


def matrix_divided(matrix, div):
<<<<<<< HEAD
    """All  elements of the matrix is divided.
=======
    """All elements of a matrix is divided.
>>>>>>> ccb1e7d633d6fd472e2effd67893e19ad6446e4b

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Note:
        matrix must be a list of lists of integers or floats, else, a TypeError
        Each row of the matrix must be of the same size, else raise a TypeError
<<<<<<< HEAD
        div must be a number (integer or floats), otherwise raise a TypeError
        div can't be equal to 0, otherwise raise a ZeroDivisionError
=======
        div must be a number (integer or float), otherwise raise a TypeError
        div can’t be equal to 0, otherwise raise a ZeroDivisionError
>>>>>>> ccb1e7d633d6fd472e2effd67893e19ad6446e4b
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
<<<<<<< HEAD
            not all((isinstance(ele, int) or isinstance(ele,float))
            for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of " "integers/floats")
=======
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
>>>>>>> ccb1e7d633d6fd472e2effd67893e19ad6446e4b

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
