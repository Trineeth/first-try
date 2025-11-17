# class Student:
#     grade = 6
#     print("hi i am a student of grade", grade)
# ob = Student()
# class Vehicle:
#     def __init__(self, ms, mileage):
#         self.max_speed = ms
#         self.mileage = mileage
#         print("object created")

# ob1 = Vehicle(240,10)
# print("models max speed is", ob1.max_speed)
# print("models mileage", ob1.mileage)
class Parrot:

    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("blu", 10)
woo = Parrot("woo", 15)
print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
