#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input
    result = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

    # Compute the square of each integer in the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][j] ** 2

    # Return the new matrix
    return result
