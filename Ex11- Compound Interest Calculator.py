#Compound Intersest Calculator using while loop

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter your Principal Amount: "))
    if principal <= 0:
        print("Please enter a Valid Principal")

while rate <= 0:
    rate = float(input("Enter your interest rate: "))
    if rate <= 0:
        print("Please enter a Valid rate of interest")

while time <= 0:
    time = int(input("Enter your time in years: "))
    if time <= 0:
        print("Please enter a Valid Time")

total = principal * pow((1 + rate/100), time)

print(f"Your total is: ₹{total:,}")
