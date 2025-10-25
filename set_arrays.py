# st = {1, 2, 3}
# print (st)
# st = {1.0, "hello", (1, 2, 3)}
# print(st)
# st = {1, 2, 3, 4, 3, 5, 6, 7, 7, 8, 9, 10}
# print(st)
# st = set([1, 2, 3, 2])
# print(st,"\n")
# numst = set([1, 2, 3, 4, 5])
# print ("original set:")
# print(numst)
# numst.pop()
# print("after removing the first element the said sat:")
# print(numst,"\n")
# x = {"green", "blue", "pink"}
# y = {"blue", "yellow"}
# print ("origianl set eliments")
# print (x)
# print(y)
# print("\nIntersection of two said sets")
# z = x.intersection(y)
# print(z)
import array as arr
arnum = arr.array('i', [1, 2, 3, 4, 5,7 , 9])
print("origenal arrey:" + str(arnum))
print ("number of times when 3 apered"+str(arnum.count(3)))
arnum.reverse()
print("revere order is:" + str(arnum))