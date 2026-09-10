#KALOKETOR

sender = str(input("sender Name: "))
item = str(input("item: "))
fragile = bool(input("Fragile? "))
weight = float(input("weight of the item :"))
distance = float(input("kilometer : "))
is_express = bool(input("is express? "))
is_international = bool(input("is international? "))

base_cost = (weight * 2.50) + (distance * 0.15)

print(base_cost)

if weight <= 2.0 and distance <= 100:
	print("Free Shipping")
else:
	print("with Shipping Fee")

#express
total = (base_cost * 1.40)
total1 = (total + 50)

#oversized
total2 = (total1 + 30)

#standard rate
total3 = (base_cost)


