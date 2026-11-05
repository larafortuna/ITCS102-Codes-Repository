u = "larajin"
p = "larajin143"

is_login = False

while is_login == False:
    user = input("USERNAME --> ")
    passw = input("PASSWORD --> ")

    if user == u and passw == p:
        print("LOGIN SUCCESSFULLY!")
        is_login = True

    else:
        print("LOGIN DENIED")
        is_login = False