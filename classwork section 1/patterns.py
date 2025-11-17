# print ("half pyramid pattern of stars (*):")
# n = int(input("enter the number of rows: "))
# for i in range(n):
#     for j in range(i + 1):
#         print("* ", end="")
#     print()

# ;6
# rowSize = int(input("enter number of rows:"))
# if rowSize%2==0:
#     halfDiamRow = int(rowSize/2)
# else:
#     halfDiamRow = int(rowSize/2)+1
# take input from user
rowSize = int(input("Enter the number of rows: "))
if rowSize % 2 == 0:  
    halfDiamRow = int(rowSize / 2)
else:
    halfDiamRow = int(rowSize / 2) + 1

space = halfDiamRow - 1


for i in range(1, halfDiamRow + 1): 
    for j in range(1, space + 1):  
        print(end=" ")
    space = space - 1
    num = 1
    for j in range(2 * i - 1):
        print(end=str(num))
        num = num + 1  
    print()

space = 1


for i in range(1, halfDiamRow): 
    for j in range(1, space + 1):  
        print(end=" ")
    space = space + 1
    num = 1
    for j in range(1, 2 * (halfDiamRow - i)):
        print(end=str(num)) 
        num = num + 1
        
    print()




