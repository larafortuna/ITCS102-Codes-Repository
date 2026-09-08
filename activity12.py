#copypasteof12 with getpass

import getpass

username = 'lara42na'
password = 'anopoun'

u = input("Enter username ----> ") 
p = getpass.getpass("Input password ----> ") 

if username == u and password == p :
	print("ACCESS GRANTED")
else :
	print("ACCESS DENIED")