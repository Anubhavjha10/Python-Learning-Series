# to find circumference of circle using math module

import math

radius = float(input("Enter the radius: "))

circumference = 2 * math.pi * radius

print(f"The circumference of the circle is {round(circumference, 2)}")