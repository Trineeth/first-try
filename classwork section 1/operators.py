# bob1 = 91
# bob2 = 60
# bob3 = 79
# bob4 = 96
# bob5 = 68
# sum = bob1+bob2+bob3+bob4+bob5

# print("the number of bobs are " + str(sum))
# average = sum // 5
# print( "the average of bob is " + str(average) )
# amount = int(input("Enter the amount of money that you want to take out:"))
# notes_1 = amount // 100
# notes_2 = (amount%100) // 50
# notes_3 = ((amount%100)%50) // 10
# notes_4 = (((amount%100)%50)%10) // 1
# print ("The amount of money you can take out is ")
# print (notes_1 , ",100 dollar bills")
# print (notes_2 , ",50 dollar bills")
# print (notes_3 , ",10 dollar bills")
# print (notes_4 , ",1 dollar bills")
print ("enter marks in these 4 subjects")
math = int(input("math:"))
science = int(input("science:"))
history = int(input("history:"))
english = int(input("english:"))
if (math > 100 or english > 100 or science > 100 or history > 100):
    print ("lier")
else  :
    sum = math+science+history+english
    average = sum//4
    print ("your average grade was " , average ,"%")
