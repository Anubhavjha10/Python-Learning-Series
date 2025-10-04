# Python Object Oriented Programing

#object = A "bundle" of related attributes (variable) and methods (functions)
#           Ex. phone, cup, book
#           You need a "class" to create many objects

#class = (blueprint) used to design the structure and layout of an object\


from car import car

car1 = car("BMW", 2023, 200400, True)
car2 = car("AUDI", 2025, 2000000, False)

print(car1.brand, car1.year, car1.clour, car1.for_sale)
car1.describe()
car1.drive()
car1.stop()