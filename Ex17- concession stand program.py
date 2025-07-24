 #concession stand program

menu = {"pizza": 9.00,
         "fries": 3.00,
         "Burgers": 6.00,
         "Chips": 25.00,
         "Maggie": 15.00,
         "Buscuit": 10.00,
         "Nacho Premium": 1000.00,
         "Cold-drinks": 210.00}

cart = []
total = 0

print("-------Menu-------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")
print("--------------")

while True:
    food = input("What food do you like?(q to quit)")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----------Your Order----------")
for food in cart:
    total += menu.get(food)
    print(food, end =" ")

print()
print(f"Total is: {total:.2f}")
print("----Thank You Visit Again!----")