import math

height = float(input("Enter the height of the Triangle: "))
base = float(input("Enter the base of the Triangle: "))

hypothenis = math.sqrt(base**2 + height**2)

print(f"The hypothenis of the Triangle is {round(hypothenis, 2)} cm")