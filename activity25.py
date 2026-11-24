def taga_triangle(num):
    for x in range(num, 0, -1):
        for y in range(1, x+1):
            print("*", end=" ")
        print()

def sum(x,y):
    return x+y

# taga_triangle(6)
# taga_triangle(4)
# taga_triangle(20)
# taga_triangle(8)

# print(sum(20, 25))
# print(sum(11, 11) * 67 // 2)

def box(size):
    for x in range(size+1):
        for y in range(size+1):
            if y == 0 or x == 0 or x == size or y == size:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def my_factorial(num):
    fact = 1
    for x in range(num, 0, -1):
        fact *= x
    return fact

# box(8)
# box(20)