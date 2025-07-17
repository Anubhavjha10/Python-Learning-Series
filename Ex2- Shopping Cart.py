# Shopping Cart Program

item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item : "))
quantity = int(input("Enter the quantity of the item in KG: "))

total = price * quantity
print(f"You buy {quantity} kg of {item}")
print(f"The total price is {total} rupee")