#  i = 1
#  while i<=5:
#     j = 1
#      while j<=10:
#          print(j, end= " ")
#          j=j+1
#      i=i+1
#     print()
# for i in range(1, 6):
#     for j in range(1,11):
#         print(j, end=' ')
#     print()
# word = input("enter in a phrase: ")
# letter = input("enter in a character: ")
# i = 0
# count = 0
# while(i < len(word)):
    
#     if(word[i] == letter):
#         count = count+1
#     i = i+1

# print ("the total number of times", letter, "is in", word, "is ", count)
num = int(input("enter a number: "))
t = num
numLen = 0
while t>0:
    numLen = numLen+1
    t = int(t/10)

if numLen>=4:
    numLen = int(numLen/2)
    chk = 0
    midTwo = 1
    while num>0:
        rem = num%10
        if chk==numLen:
            midOne = rem
        elif chk==(numLen/10):
            midTwo = rem
        num = int(num/10)
        chk = chk+1
    prod = midOne*midTwo
    print ("\nProduct of mid digits", prod)
else:
    print("it is not a 4 or more digit number")