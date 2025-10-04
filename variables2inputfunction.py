# This is my first python Program
print("Hello User!")
print("I am anubhav")

# Variables

#strings
first_name = 'Anubhav'
food = 'Mangoes'
email = 'anubhavjha424@gmail.com'

print(first_name)
print(f"Hello {first_name}")
print(f"You Like {food}")
print(f"Your Email is {email}")

#integers
age = 20
quantity = 4
print(f"You are {age} years old")
print(f"You are buying {quantity} mangoes")


# floats
price = 15.30
percent = 79.5
distance = 10.5
print(f"The Price of Mangoes is {price}")
print(f"Your Percentage is {percent}")
print(f"The Distance from School to Home is {distance} KM")

#boolean
is_student = True
for_sale = True
if is_student:
    print("You are a Student")
else:
    print("You are a Teacher")

if for_sale:
    print("Car is Avillable")
else:
    print("Car is Not avillable")

#typecasting = the process in which a variable from one data type are converting into another str() int() float() bool()

#to check what type of type we use print(type())
#Example
print(type(first_name))

#assign the age variable to percentage
age = int(percent)
print(age)


#input() function

name = input("What's your name : ")
umar = int(input("How old are you? : "))
#umar = int(umar)
umar += 1

print(f"Hello {name}")
print("Happy Bithday!")
print(f"Your age is {umar}")
