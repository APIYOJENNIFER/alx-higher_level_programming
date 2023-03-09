#!/usr/bin/python3
def main():
    from sys import argv
    total_sum = 0
    for i in range(len(argv)):
        if i > 0:
            total_sum += int(argv[i])
    print(total_sum)


if __name__ == "__main__":
    main()
