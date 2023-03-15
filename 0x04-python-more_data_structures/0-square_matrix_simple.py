#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    Returns a new matrix:
        - Same size as matrix
        - Each value should be the square of the value of the input
    Initial matrix should not be modified
    """
    # Create a new matrix with the same dimensions as the input matrix
    result = [[0 for c in range(len(matrix[i]))] for j in range(len(matrix))]

    # Compute the square value of each element of the input matrix
    for j in range(len(matrix)):
        for c in range(len(matrix[j])):
            result_matrix[j][c] = matrix[j][c] ** 2

    return result_matrix
