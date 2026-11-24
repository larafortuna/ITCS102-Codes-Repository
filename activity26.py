from activity25 import taga_triangle
from activity25 import box
from activity25 import sum
from activity25 import my_factorial

while True:
    print("MINI MENU")
    print("SELECT AN OPTION")
    print("1 - Triangle\n2 - SUM\n3 - Box\n4 - Factorial\n5 - EXIT")
    choose = int(input("WHICH OPTION TO GO? "))

    if choose == 1:
        print("TAGA TRIANGLE")
        size = int(input("Size ng Triangle --> "))
        taga_triangle(size)
        continue

    elif choose == 2:
        print("SIMPLE SUMMATION")
        num1 = int(input("number 1 --> "))
        num2 = int(input("number 2 --> "))
        print(f"the sum of {num1} and {num2} is {sum(num1. num2)}")
        continue

    elif choose == 3:
            print("SIMPLE SUMMATION")
            num1 = int(input("number 1 --> "))
            num2 = int(input("number 2 --> "))
            print(f"the sum of {num1} and {num2} is {sum(num1. num2)}")
            continue