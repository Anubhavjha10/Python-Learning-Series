#while loop = execute the code while some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You didn't enter a name\nPlease try again")
    name = input("Enter your name: ")

age = input("Enter your age: ")

while age == "":
    print("You didn't enter an age or wrong age entered\nPlease try again")
    age = input("Enter your age: ")


print(f"Hello {name}!")
print(f"Your age is {age}.")

