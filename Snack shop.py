snack_name = "Chips"
price = 2.50
quantity = 5
snack_available = True

print("snack_name:", snack_name)
print("price:", price)
print("quantity:", quantity)
print("snack_available:", snack_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(snack_available))

total = price * quantity
print("total value: $:, total")
print("sale price: $", -0.25)
print("double stock:", quantity * 2)

print("is the price is under 2?", price < 2)
print("more than 5 in stock", quantity > 5)
print("is price exactly $1.50?", price == 1.50)

shop_name = "First"+" "+"bite"
print("shop name:", shop_name)
print("letters in snack name:", len(snack_name))
print("first letter in the snack name:", snack_name[0])

price_a = 3.00
price_b = 1.50
print("before:", price_a, "after", price_b)

temp = price_a
price_a = price_b
price_b = price_a