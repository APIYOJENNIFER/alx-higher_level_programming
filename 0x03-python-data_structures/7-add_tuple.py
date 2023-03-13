#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    if len(tuple_a) < 2:
        tuple_a = (0, 0)
    if len(tuple_b) < 2:
        tuple_b = (0, 0)
    if len(tuple_a) > 2:
        tuple_a = (tuple_a[0], tuple_a[1])
    if len(tuple_b) > 2:
        tuple_b = (tuple_b[0], tuple_b[1])

    i, j = tuple_a
    x, y = tuple_b

    a = i + x
    b = j + y

    tuple_x = (a, b)
    return tuple_x


if __name__ == "__main__":
    add_tuple()
