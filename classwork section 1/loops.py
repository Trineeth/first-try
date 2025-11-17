# n = int(input("enter the number whose sum you want: "))
# sum = 0

# for i in range(1, n+1):
#     sum = sum+i
#     print ("\nsum = ", sum)
# string = input("please enter a word and this will reverse it : ")
# string2 = ('')
# for i in string:
#     string2 = i + string2

# print ("n\The original word is", string)
# print ("n\the reversed word is", string2)     
n = int(input("enter the value of n"))
print ("the numbers of {0} to {1} are:".format(n,1))
for i in range(n,0,-1):
    print (i)