# tupl = ("tuple", False, 3.2, 1)
# print (tupl)
# tupl = (4, 6, 2, 8, 3, 1)
# print(tupl)
# tupl = tupl + (9, )
# print (tupl)
# tup = (50, 10, 60, 70, 50)
# print(tup.count(50))
# slic = tupl[3:5]
# print(slic)
# slic = tupl[:6]
# print(slic)
def palin(r):
    e = len(r) - 1
    s = 0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

a = int(input("enter in a number"))
b = int(input("enter in a number"))
c = int(input("enter in a number"))
d = int(input("enter in a number"))
e = int(input("enter in a number"))
f = int(input("enter in a number"))

r = (a,b,c,d,e,f)
print(r)
if(palin(r)):
    print("the tuple is flip flop")
else:
    print("the tuple is not flip flop")