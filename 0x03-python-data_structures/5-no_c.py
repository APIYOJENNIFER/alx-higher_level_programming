#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] == "C":
            my_string = my_string[:i] + my_string[i+1:]
            return my_string
        else:
            final_string = my_string[:len(my_string)]
    str_copy = my_string[:]
    for j in range(len(str_copy)):
        if str_copy[j] == "c":
            str_copy = str_copy[:j] + str_copy[j+1:]
            return str_copy
        else:
            str_copy = str_copy[:len(str_copy)]


if __name__ == "__main__":
    no_c()
