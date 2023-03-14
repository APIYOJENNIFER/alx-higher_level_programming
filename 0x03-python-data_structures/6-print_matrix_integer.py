#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in matrix[i]:
            if matrix[i].index(j) == 2:
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
        print("")


if __name__ == "__main__":
    print_matrix_integer()
