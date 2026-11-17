fruit_basket = []

fruit_basket = ["saging", "mangga", "papaya", "rambutan", "duhat"]
print(fruit_basket)

fruit_basket.append("grapes")
fruit_basket.append("bayabas")
fruit_basket.append("melon")
fruit_basket.append("lemon")
fruit_basket.append("apple")
print(fruit_basket)
fruit_basket.insert(3, "orange")
print(fruit_basket)

fruit_basket.pop(4)
fruit_basket.remove('duhat')
print(fruit_basket)

print(fruit_basket[0 : 5])