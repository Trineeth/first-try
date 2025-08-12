# units = int(input("how many units have you consumed:"))
# if (units < 50):
#     amount = units * 2.60
#     surcharge = 25
# elif (units <= 100):
#     amount = 130 + ((units - 50) * 3.25)
#     surcharge = 35
# elif (units <= 200):
#     amount = 130 + 162.5  + ((units - 100) * 5.26)
#     surcharge = 45
# else:
#     amount = 130 + 162.5 + 526 + ((units - 200) * 8.45)
#     surcharge = 75


# tot = surcharge + amount
# print ("elecriciry bill is equal to" , tot)
print ("choose your veichle")
print ("1. bike")
print ("2. car")
choice = int(input("what is your awnser:"))

if (choice == 1):
    print ("do you like")
    print ("1 scooter")
    print ("2 scooty")
    choice2 = int(input("choose:"))
    if (choice2 == 1):
        print ("you like scooters")
    else:
        print ("you like scootys")
elif (choice == 2):
    print ("do you like")
    print("1 XUV")
    print("2 Sedan")
    choice2 = int(input("what is your awnser:"))
    if (choice2 == 1):
        print ("you like XUV")
    else:
        print ("you like sedans")

else:
    print ("wrong choice")