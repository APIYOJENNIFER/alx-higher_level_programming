#!/usr/bin/python3
def calc():
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i in range(len(argv)):
        op = argv[2]
        a = argv[1]
        b = argv[3]
        if op == "+":
            print("{} {} {} =".format(a, op, b), add(int(a), int(b)))
            exit(0)
        elif op == "-":
            print("{} {} {} =".format(a, op, b), sub(int(a), int(b)))
            exit(0)
        elif op == "*":
            print("{} {} {} =".format(a, op, b), mul(int(a), int(b)))
            exit(0)
        elif op == "/":
            print("{} {} {} =".format(a, op, b), div(int(a), int(b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    calc()
