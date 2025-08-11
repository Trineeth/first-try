# a = 1
# if not a :
#     print("True")
# else:
#     print ("false")
# a = 12
# b = -12
# c = 0
# if (b > 0 or c > 0):
#     print ("either the number is greater than 0")
# else:
#   print ("no number is greater than 0")
# if (b > 0 or a > 0):
#     print ("either the number is greater than 0")
# else:
#     print ("no number is greater than 0")
hieght = float(input("what is your hieght in cm: "))
weight = float(input("what is your wieght in kg: "))
bmi = weight / (hieght / 100)**2
if bmi <= 18.4:
    print ("you are underweight")
elif bmi <= 24.9:
    print ("you are healthy")
elif bmi <= 29.9:
    print ("you are overweight")
elif bmi <= 34.9:
    print ("you are servrly overweight")
elif bmi <= 39.9:
    print ("you are obese")
else:
    print ("you are servly obese")
