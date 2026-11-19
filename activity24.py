#BEEPBEEPBEEPANGSABINGJEEP
route = ["Termial", "DLL", "Perez Park", "QNHS", "Pacific Mall"]
passengers = []
SEATS = 6
FARE = 13
total = 0

while True:
    print()
    print("Welcome sa Jeepney ni Lara ft. Yeng Constantino :)")
    print("Hop in : Sakay na! :", passengers)
    print(len(passengers), "of", SEATS, "seats")
    print("1 - Sakay\n2 - Priority Seat\n3 - Tabi lang po, manong!")
    print("4 - Baba sa pinto\5 - Baba sa harap")
    print("6 - Seat check\n7 - Balikan\n8 - Exit")
    choice = input("Choice: ")

    if choice == "1":
        if len(passengers) == SEATS:
            print("Puno na po, sorry")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + FARE
            print(name, "boarded at the back.")

    elif choice == "2":
        if len(passengers) == SEATS:
            print("Puno na po, sorry")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + FARE
            print(name, "took the priority seat")

    elif choice == "3":
        name = input("Sino ang bababa ka ba ka ba? ")
        if name in passengers:
            passengers.remove(name)
            print(name, "got off. Ingat sila sayo! ")
        else:
            print(name, "sino yan, wala naman yan dito bruh")

    elif choice == "4":
        if len(passengers) == 0:
            print("Walang pasahiru busing")
        else:
            left = passengers.pop()
            print(left, "umalis na dumaan sa door.")

    elif choice == "5":
        if len(passengers) == 0:
            print("Wala pang pasahiru ang jeepney ni yeng")
        else:
            front = passengers.pop(0)
            print(front, "lumabas sa harap")

    elif choice == "6":
        for i in range(len(passengers)):
            print("Seat", i + 1, passengers[i])

    elif choice == "7":
        route.reverse()
        print("Route: ", route)

    elif choice == "8":
        print("Total fare today: ", total)
        break

    else:
        print("Invalid choice.")