#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        new_list = set(my_list)
        total = sum(new_list)
        return total


if __name__ == "__main__":
    uniq_add()
