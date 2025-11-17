# class Vehicle:
#     def __init__(self,name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass


# School_bus = Bus("School Volvo", 180, 12)
# print("Vehicle name: ", School_bus.name, "speed: ", School_bus.max_speed, "Vehicle mileage: ", School_bus.mileage,)
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class Employee(Person):
    def __init__(self, name, idnumber, salery, post):
        self.salery = salery
        self.post = post
        Person.__init__(self, name, idnumber)

a = Employee('Rahul', 886012, 200000, "Intern")
a.display()