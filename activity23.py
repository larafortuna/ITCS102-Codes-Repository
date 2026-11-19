bruno_mars = []
taylor_swift = []
bruno_major = []
justin_bieber = []
bongbongmarcos = []

while True:
    ans = input("Do you listen to music --? yes/no ").lower()

    if ans == "yes":
        print("ARTISTS LIST YOU MUST KNOW: ")
        print("1-bruno_mars \n2-taylor_swift\n3-bruno_major\n4-justin_bieber\n5-bongbongmarcos")
        choice = int(input("Who's artists you are familiar with?"))

        if choice == 1:
            print("Bruno Mars selected.")
            song = input("Put a song u know --> ")
            bruno_mars.append(song)
            print("list of bruno mars:\n", bruno_mars)
            con = input("Do you wish to continue yes / no ").lower()
            if con == "yes":
                continue
            else:
                break

        elif choice == 2:
            print("Taylor Swift selected.")
            song = input("Put a song u know --> ")
            taylor_swift.append(song)
            print("list of taylor swift songs\n:", taylor_swift)
            con = input("Do you wish to continue yes / no ").lower()
            if con == "yes":
                continue
            else:
                break

        elif choice == 3:
            print("Bruno Major selected.")
            song = input("Put a song u know --> ")
            bruno_major.append(song)
            print("list of bruno major songs:\n", bruno_major)
            con = input("Do you wish to continue yes / no ").lower()
            if con == "yes":
                continue
            else:
                break
  
        elif choice == 4:
            print("Justin Bieber")
            song = input("Put a song u know --> ")
            justin_bieber.append(song)
            print("list of Justin Bieber songs:\n", justin_bieber)
            con = input("Do you wish to continue yes / no ").lower()
            if con == "yes":
                continue
            else:
                break

        elif choice == 4:
            print("(BO)ng (BO)ng Marcos selected")
            song = input("Put a song u know --> ")
            bongbongmarcos.append(song)
            print("list of BongBong Marcos songs:\n", bongbongmarcos)
            con = input("Do you wish to continue yes / no ").lower()
            if con == "yes":
                continue
            else:
                break

    else:
        print("INVALID CHOICE")