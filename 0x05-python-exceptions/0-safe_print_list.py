#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            n += 1
    except IndexError:
        print()
        return n
    print()
    return n


if __name__ == "__main__":
    safe_print_list()
