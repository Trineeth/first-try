# for i in range(9):
#     if i==6:

        
#         continue
#     if i ==6:

#         break
    
#     print(i)

# a = input ("enter a word: ")
# for i in a:
#     if (i == 'a'):
#         print ("a  is found")
#         break
#     else:
#         print("a is not found")
# a = int(input("enter in a number"))
# b = 0
# c = 0
# d = 0
# e = 0
# for x in range(a):
#     if x % 20 == 0:
#         print("twist")
    
#     elif x % 15 == 0:
#         print("pass")
#         b = b+1
#         pass
        
#     elif x % 10 == 0:
#         c = c+1
#         print("fizz")
#     elif x % 5 == 0:
#         d = d+1
#         print("buzz")
#     elif x % 3 == 0:
#         e = e+1
#         print("ding")
#     else:
#         print(x)
# print("number of passes is ", b)    
# print("number of fizzes is ", c)
# print("number of buzzes is ", d)
# print("number of dings is ", e)      
f = int(input("enter in a number: "))
var = f
while var > 0:
    var = var - 0.1
    if var % 5 == 0:
        continue
    print("\nCurrent varible value = ", var)
print("\ngood bye")