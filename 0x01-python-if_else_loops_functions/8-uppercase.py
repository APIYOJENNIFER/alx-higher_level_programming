#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if(97 <= ord(str[i]) <= 122):
            asc_upper = ord(str[i]) - 32
            upper = chr(asc_upper)
            if(i == (len(str) - 1)):
                print("{}".format(upper))
            else:
                print("{}".format(upper), end="")
        else:
            print("{}".format(str[i]), end="")
