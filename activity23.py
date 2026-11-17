bruno_mars = []
taylor_swift = []
bruno_major = []
avril_lavigne = []
bongbongmarcos = []

while True:
    ans = input("Do you listen to music --? yes/no ").lower()

    if ans == "yes":
        print("Who's artists you are familiar with? ")
        print("1- bruno_mars \n2-taylor_swift\n3-bruno_major\n4-avril_lavigne\n5bongbongmarcos")

        choice = int(input("Input --> "))

        if choice == 1:
            print("bruno mars ")
            song = input("Put a song u know --> ")
            bruno_mars.append(song)
            print("list of bruno mars")
            print(bruno_mars)
            con = input("Do you wish to continue yes / no ").lower()
            continue
        else:
            break
    else:
        print("INVALID choice")