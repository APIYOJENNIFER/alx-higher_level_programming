#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    if new_list is not None:
        for i in range(len(new_list)):
            if new_list[i] == search:
                new_list[i] = replace
        return new_list


if __name__ == "__main__":
    search_replace()
