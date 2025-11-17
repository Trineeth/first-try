# class square:
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         print ("my area is: ", self.side**2)
# class circle:
#     def __init__ (self, radius):
#         self.radius = radius

#     def area(self):
#         print("my area is:  ", 3.14*self.radius*self.radius)
# osquare = square(5)
# ocircle = circle(5)

# osquare.area()
# ocircle.area()
from abc import ABC , abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("passed value: ", x)
    @abstractmethod
    def task(self):
        print("we are in ABC class")

class text_class(Absclass):
    def task(self):
        print ("we are in text_class task")

test_obj = text_class()
test_obj.task()
test_obj.print(100)