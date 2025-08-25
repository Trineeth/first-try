import random
# playing = True
# number = str(random.randint(0,11))
# print ("i have chosen a random number but u have to guess it from the numbers between 0 to 9")
# print("the game ends when you guess one right")
# while playing:
#     guess = input("give me your best guess: ")
#     if number == guess:
#         print ("you win the game")
#         print ("the number was ", number)
#         break
#     else:
#         print("you guessed wrong u may play again")
#         number = str(random.randint(0,11))
while True:
    user_action = input("enter in a choince(rock , paper,scissors): ")
    possiable = ["rock", "paper", "scissors"]
    copmputrer = random.choice(possiable)
    print("you can choose between enter in a choince rock , paper,scissors")
    if user_action == copmputrer:
        print("you both choose the same awnser")