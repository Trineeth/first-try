# a = 5
# b = 3
# print (a&b)
# print (a|b)
# print (a^b)
# x = 5.0
# if (type(x) is int):
#     print ("true")
# else:
#     print ("false")
# a = 10
# b = -10
# print ("a >> 1 = ", a >> 1)
# print ("b >> 1 = ", b >> 1)
# a = 5
# b = 10
# print ("a << 1 = ", a << 1)
# print ("b << 1 = ", b << 1)
print ("enter your grades for these subjects")
history = int(input("history:"))
science = int(input("science:"))
english = int(input ("english:"))
math = int(input("math:"))
reading = int(input("reading:"))
tot = history+science+english+math+reading
av = tot/5
if (av >= 91 and av <= 100):
    print ("your average is A" )