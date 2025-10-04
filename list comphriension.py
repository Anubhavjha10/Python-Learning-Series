 #list comphrension = A concise way to create lists in python
#                  Compact and easier to read than traditional loops
#                  Expressions for value it iterable if condition

doubles = []
for x in range(1,11):
    doubles.append(x * 2)

print(doubles)
aj = [x * x for x in range(1,11)]
print(aj)

fruits = ["apple", "banana", "cherry"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)