# Iterables = An object/collection that cN RETURN ITS element one at a time, allowing it to be iterated over in a loop

numbers =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

# for tuples
numbers =  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for number in numbers:
    print(number)

# for sets
# sets are not reversible
#fruits = {'apple', 'banana', 'cherry'}
#for fruit in reversed(fruits):
 #   print(fruit)

fruits = {'apple', 'banana', 'cherry'}
for fruit in fruits:
    print(fruit)

# for string

name = "Anubhav Jha"

for character in name:
    print(character, end= "-")

# for dictionary
my_dic = {"A": 1, "B": 2, "C": 3}
for key in my_dic:
    print(key)
