# class myClass:
#     __privateVar = 27
#     def __privmath(self):
#         print ("I'm inside class myClass")
#     def hello(self):
#         print ("Private Varible value: ",myClass.__privateVar)

# foo = myClass()
# foo.hello()
# foo.__privmath
# class Computer:
#     def __init__(self):
#         self.__mp = 900

#     def sell(self):
#         print("Selling price: {}".format(self.__mp))
#     def setMP(self, price):
#         self.__mp = price

# c = Computer()
# c.sell()

# c.__mp = 1000
# c.sell()
# c.setMP(1000)
# c.sell()
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return"({0}, {1})".format(self.x, self.y)
    
p1 = Point(2, 3)
print(p1)