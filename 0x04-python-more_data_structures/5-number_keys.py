#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    if a_dictionary is not None:
        for i in enumerate(a_dictionary):
            x, y = i
            num = x + 1
        return num


if __name__ == "__main__":
    number_keys()
