#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value


if __name__ == "__main__":
    update_dictionary()
