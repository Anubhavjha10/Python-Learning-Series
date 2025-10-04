#static methods = A method that belongs to a class rather than any object from that class (instance)
#                 usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def get_info(self):
        return f"{self.name} = {self.job}"

    @staticmethod
    def is_valid_job(job):
        valid_jobs = ["manager", 'cahier', 'cook', 'chef']
        return job in valid_jobs

employee1 = Employee("John", "manager")
employee2 = Employee("Jane", "chef")
employee3 = Employee("Doe", "no jo")

print(Employee.is_valid_job("scientist"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())