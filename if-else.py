# if = do some code if same condition is true
# else do somthing else

age = int(input("How old are you? =  "))

if age >= 18:
    print("You are In")
elif age < 0:
    print("LOL! You are Not Born. ")
else:
    print("You are Out")

#Example 2

name = input("What is your name? ")

if name == "":
    print("You are Not enter your Name")
else:
    print(f"Hello {name}")
    print("Welcome to Our House")

# Example 3(boolean)

for_sale = True
if for_sale:
    print("Car is Avillable")
else:
    print("Car is Not Avillable")