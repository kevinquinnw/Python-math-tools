import numpy as np


def matrix_multiplication(first_matrix: list, second_matrix: list) -> list:
    """Take any n x n matrix and multiply them together."""

# First want to transform the second matrix into an array of columns.
    new = []
    for i in range(len(second_matrix)):
        new.append([item[i] for item in second_matrix])

    newer = []
    for j in range(len(first_matrix)):
        for k in range(len(new)):
            newer.append(sum([a * b for a, b in zip(first_matrix[j], new[k])]))

    chunks = []
    for i in range(0, len(newer), len(first_matrix)):
        chunks.append(newer[i:i+len(first_matrix)])

    return chunks


def numpy_matrix_multiplication(first_matrix: list, second_matrix: list) -> np.array:
    """Using numpy for matrix multiplication."""
    first_m = np.array(first_matrix)
    second_m = np.array(second_matrix)

    return np.dot(first_m, second_m)


def matrix_mult(first_matrix: list, second_matrix: list) -> list:
    """More efficiently"""
    zipped_second = list(zip(*second_matrix))
    return [[sum(a * b for a, b in zip(row_a, col_b))
             for col_b in zipped_second] for row_a in first_matrix]
