# def greet(name, message='hi'):
#     return f"{message} {name}"

# greeting = greet('john', 'hello') 
# print(greeting)

# def tot_cal(bill,tip):
#     total = bill * (1 + 0.01*tip)
#     total = round(total,2)
#     print(f"please pay ${total}")
# tot_cal(150,20)
# def cube(number):
#     return number*number*number 
# def by_3(number):
#     if number %3 ==0:
#         return cube(number)
#     else:
#         return False
# print(by_3(9))
# print(by_3(4))
def factorial(x):
    '''this is a recursive factorial fuction to find the factorial of an intergir '''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print (factorial.__doc__)
print("the factorial of 0", factorial(0))
print("the factorial of 1", factorial(1))
print("the factorial of 2", factorial(2))
print("the factorial of 3", factorial(3))
print("the factorial of 4", factorial(4))
print("the factorial of 5", factorial(5))