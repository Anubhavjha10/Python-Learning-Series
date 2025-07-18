print('Welcome to Weight Calculator\nIn this you convert kilogram into pound and Pound into kilogram')
weight = float(input("Enter weight: "))
unit = input("Enter the unit(K or L): ")

if unit == "K" or "k":
    weight = weight * 2.205
    print(f"Your weight is {round(weight, 3)} Pounds")
elif unit == "L" or "l":
    weight = weight / 2.205
    print(f"Your weight is {round(weight, 3)} kilograms")
else:
    print("Invalid input")