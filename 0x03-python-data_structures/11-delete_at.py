#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is not None:
        if idx < 0 or idx > len(my_list) - 1:
            return my_list
    for i in range(len(my_list)):
        if i == idx:
            my_list = my_list[:i] + my_list[i + 1:]
    return my_list


if __name__ == "__main__":
    delete_at()
