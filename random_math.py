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
    user_action = input("Enter a choice (rock, paper, scissors): ") 
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")  
    
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break

    