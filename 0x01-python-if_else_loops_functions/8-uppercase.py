#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in range(len(str)):
        if (97 <= ord(str[i]) <= 122):
            asc_upper = ord(str[i]) - 32
            upper = upper + chr(asc_upper)
        else:
            upper = upper + str[i]
    print("{}".format(upper))
