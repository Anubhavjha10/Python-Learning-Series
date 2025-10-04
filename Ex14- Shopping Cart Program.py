# Shopping Cart Program Using List Set and Tupples

foods = []
prices = []
total = 0

while True:
    food = input("Enter food name (q to quit)= ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter price of {food}: " ))
        foods.append(food)
        prices.append(price)

print("----- Your CART -----")

for food in foods:
    print(food, end = " ")

for price in prices:
    total += price
    print()
    print(f"Your cart total is {total}")