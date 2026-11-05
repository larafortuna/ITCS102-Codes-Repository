sum = 0

gow = True
while gow == True:
    x = int(input("Guess my age from 1-25 --> "))

    if x == 19:
        print("Correct! Loop Terminated")
        break
    else:
        print("Engk Wrong! Continue Loop")
        continue