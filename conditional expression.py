#conditional expression = A oneline shortcut for the if-else statement(ternary operators)
                        #Print or assign one of two values based on a condition
                        #X if condition else Y

#Example number is positive or negative
num = 5
print("Positive" if num > 0 else "Negative")

#Example of number is eve or odd
num1 = 4
print("Even" if num1 % 2 == 0 else "Odd")

#Example check number is maximun
a = 3
b = 4
print(a if a > b else b)

#Example check number is minimum
c = 10
d = -1
print(c if c < d else d)

#Example of check peerson is underage or aged
age = 18
print("Welcome to our house" if age > 18 else "Sorry you are Child")

#Example of check temprature is cold aur hot
temp = 22
print("Cold" if temp <= 21 else "Hot")

#Example of access of admin
user = "admin"
print("Full access" if user == "admin" else "Limited Access")