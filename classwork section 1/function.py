# def wishes():
#     print("hello")
#     print("how are you doing")

# wishes()

# def weather():
#     print ("the wheather is nice in", spring)
#     print ("which is the same as", autum)
# spring = ("autum")
# autum = spring
# weather()
def add(P, Q):
    return P + Q
def sub(P, Q):
    return P - Q
def mul(P, Q):
    return P * Q
def div(P, Q):
    return P / Q

print ("choose betewene:")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
choice = int(input("enter in one of the choices: "))
num1 = int(input("enter in your number: "))
num2 = int(input("enter in your second number: "))
rest = 0
if choice == 1:
    print(add(num1, num2))
elif choice == 2:
    print(sub(num1,num2))
elif choice == 3:
    print(mul(num1,num2))
elif choice == 4:
    print(div(num1,num2))
else:
    print("invalid input")


