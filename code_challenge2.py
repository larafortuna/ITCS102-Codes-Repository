#nagugutom na po akoh
money = 6767

print("Money to deposit -->", money) 

#Money to deposit
thousand = money // 1000
money = money - thousand * 1000

five = money // 500
money = money - five * 500

two = money // 200
money = money - two * 200

one = money // 100
money = money - one * 100

sixty = money // 60
money = money - sixty * 60

seven = money // 7
money = money - seven * 7

print("You have", thousand, "of 1000")
print("You have", five, "of 500")
print("You have", two, "of 200")
print("You have", one, "of 100")
print("You have", sixty, "of 60")
print("You have", seven, "of 7")
