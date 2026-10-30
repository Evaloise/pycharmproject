# Class is a blueprint of an object
#  is an instance of a class

class Employee:

    def __init__(self, name, gender, position, age):
        self.name = name
        self.gender = gender
        self.position = position
        self.age = age

    @staticmethod
    def drive():
        print("Employee is driving")

    @staticmethod
    def eat():
        print("Employee is eating")


# Creating objects
employee1 = Employee(name="Mark", gender="Male", position="CEO", age=57)
print(employee1.name, employee1.gender, employee1.position, employee1.age)

employee2 = Employee(name="Mary", gender="Female", position="Manager", age=30)
print(employee2.name, employee2.gender, employee2.age)

employee3 = Employee(name="John", gender="Male", position="Developer", age=25)
print(employee3.name, employee3.gender, employee3.age)
