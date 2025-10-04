# class methods = allow opreations related to the class itself
#                 Take (self) as the first parameters, which represents the class itself

class students:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        students.count += 1
        students.total_gpa += gpa


    #Instance Method
    def get_info(self):
        return f"{self.name} =  {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total of students: {cls.count}"

    @classmethod
    def get_total_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count}"

student1 = students("John", 3.14)
student2 = students("DP", 3.14)
student3 = students("JP", 4.14)

print(student1.get_count())
print(students.get_total_gpa())