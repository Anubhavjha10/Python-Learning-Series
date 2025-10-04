#class variables = shared amoung all instances of a class
#                  Defined outside the constuction
#                  Allow you to share data amoung all objects created from that class


class student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.num_students += 1

student1 = student("OM", 12)
student2 = student("Vishal", 20)
student3 = student("Ashley", 18) 

print(student1.name, student1.age, student1.class_year)
print(student.num_students)
