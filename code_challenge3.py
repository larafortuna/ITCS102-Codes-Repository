#KALKOLETOR

sender = str(input("sender Name: "))
item = str(input("item: "))
fragile = input("Fragile? ") == "true"
weight = float(input("weight of the item :"))
distance = float(input("kilometer : "))
is_express = input("is express? ") == "true"
is_international = input("is international? ") == "true"

#basecost
base_cost = (weight * 2.50) + (distance * 0.15)

#bigatatlayo
if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
    category = "Free Shipping"
    total = 0

#express
elif is_express and is_international:
    category = "Express International"
    total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight > 20):
    category = "Express or Heavy International"
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    category = "Oversized"
    total = base_cost + 30

else:
    category = "Standard Rate"
    total = base_cost

print("\n--- SHIPPING DETAILS ---")
print("Sender:", sender)
print("Item:", item)
print("Weight:", weight, "kg")
print("Distance:", distance, "km")
print("Category:", category)
print("Total Amount: PHP{:.2f}".format(total))
print("\t\t\tThankyou for shopping with us!\n\t\t\t\t", sender)
