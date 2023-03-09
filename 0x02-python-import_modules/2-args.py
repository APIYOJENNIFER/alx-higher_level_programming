#!/usr/bin/python3
def main():
    from sys import argv
    if len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
    elif len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))
    for i in range(len(argv)):
        if i > 0:
            print("{}: {} ".format(i, argv[i]))


if __name__ == "__main__":
    main()
