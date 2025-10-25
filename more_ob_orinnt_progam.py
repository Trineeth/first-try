# class IOString():
#     def __init__ (self):
#         self.str1 = ""
#     def get_String(self):
#         self.str1 = input("enter string: ")
#     def print_String(self):
#         print("the result is: ", self.str1.upper())
# str1 = IOString()
# str1.get_String()
# str1.print_String()
# class Employee:
#     def __init__(self):
#         print("employee created")

#     def __del__(self):
#         print("destructer called")
# def Create_obj():
#     print("making object...")
#     obj = Employee()
#     print("function end")
#     return obj
# print('calling Create_obj() function...')
# obj = Create_obj()
# print("program end")
class pair_elaments:
    def twoSum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target-num], i )
            lookup[num] = i

value = int(input("enter sum for you want to make this search: "))
print("index1=%d, index=%d" %
pair_elaments().twoSum((10,20,30,40,50,60,70),value))