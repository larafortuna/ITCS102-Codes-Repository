rows = int(input("Enter number of rows --> "))

for a in range(rows):
    for b in range(rows - a -1):
        print(" ", end=" ")

    for c in range(rows):
        if a == 0 or a == rows - 1 or c == 0 or c == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()