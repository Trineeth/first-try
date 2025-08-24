# try:
#     num = int(input("enter a number in: "))
#     print("the number you entered is ", num)
# except ValueError as ex:
#     print("exeption ", ex)
# try:
#     num1, num2 = eval(input("enter in a number, seperated by a comma: "))
#     result = num1 / num2
#     print("the result is ", result)
# except ZeroDivisionError:
#     print("divsion by zero is error")
# except SyntaxError:
#     print("the comma is missing (1 , 2)")
# except:
#     print("wrong input")
# else:
#     print("no exeptions")
# finally:
#     print("this will exicute no matter what")
# valid = False
# while not valid:
#     try:
#         n=int(input("enter a number: "))
#         while n%2==0:
#                 print ("bye")
#         valid = True
#     except ValueError:
#          print("invalid")
# try:
    
#     age = int(input("enter your valid age: "))
#     if (age<18):
#         raise ValueError
#     else:
#         print("the age is valid")
# except ValueError:
#     print("The age is not valid")
try:
    k = 5
    print(b)
except NameError:
    print("varable not defined")
print("test")