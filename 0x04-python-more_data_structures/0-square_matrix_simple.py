#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        return [[x*x for x in matrix[x]] for x in range(len(matrix))]


if __name__ == "__main__":
    square_matrix_simple()
