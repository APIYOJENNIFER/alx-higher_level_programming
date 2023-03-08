#!/usr/bin/python3
def fizzbuzz():
    mult_three = []
    mult_five = []
    for i in range(1, 101):
        mult_three.append(i*3)
        mult_five.append(i*5)
        if i in mult_three and i in mult_five:
            print("FizzBuzz ", end="")
        elif i in mult_three:
            print("Fizz ", end="")
        elif i in mult_five:
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")
