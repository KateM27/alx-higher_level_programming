#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = list(map(lambda a: list(map(lambda b: b**2, a)), matrix))
    return new_matrix
