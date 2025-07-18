print("Calculator")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operators = input("Enter the operator you want to continue with (+, -, *, /) = ")

if operators == "+":
    result = num1 + num2
    print(f"Your answer is: {round(result, 3)}")
elif operators == "-":
    result = num1 - num2
    print(f"Your answer is: {round(result, 3)}")
elif operators == "*":
    result = num1 * num2
    print(f"Your answer is: {round(result, 3)}")
elif operators == "/":
    result = num1 / num2
    print(f"Your answer is: {round(result, 3)}")
else:
    print("Invalid operator")