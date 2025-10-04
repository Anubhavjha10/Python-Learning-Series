print("Welcome to Temprature Conversion Calculator")

temp = float(input("Enter temperature: "))
unit = input("Enter unit(C or F): ")

if unit == "C" or "c":
    temp = (temp * 9/5) + 32
    print(f"Temprature is: {round(temp, 3)} F")
elif unit == "F" or "f":
    temp = (temp - 32) * 5/9
    print(f"Temprature is: {round(temp, 3)} C")
else:
    print("Invalid Temprature Unit")