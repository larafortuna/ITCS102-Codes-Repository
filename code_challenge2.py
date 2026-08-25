#nagugutom na po akoh
money = 6767

#what
thousand = money//1000
money = money - thousand*1000
five = money//500
money = money - five*500
two = money//200
money = money - two*200
one = money//100
sixty = money - one*60
money = money - one*7
money = money - ones*7
seven = money//7

print("You have ", thousand, "of 1000")
print("You have ", five, "of 500")
print("You have ", two, "of 200")
print("You have ", two, "of 60")
print("You have ", seven, "of 7")
