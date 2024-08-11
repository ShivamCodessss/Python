# Rock Paper Scissors

import random
play = input("Do want to play the Rock Paper Scissor Game: ").lower()

if play != "yes":
    print("See You Soon")
    quit()
else:
    print("That's the Spirit")

options = ["Rock", "Paper", "Scissor"]

UserInput = input("Enter Your Choice: (Rock, Paper, Scissor) ").lower()

Computer_choice = random.choice(options)

print(f"You Choose: {UserInput}")
print(f"Computer Choose: {Computer_choice}")


if UserInput == Computer_choice:
    print("It's a tie!")
elif UserInput == "Rock" and Computer_choice == "Scissor":
    print("You Win ! ")
elif UserInput == "Paper" and Computer_choice == "Rock":
    print("You Win !")
elif UserInput == "Scissor" and Computer_choice == "Paper":
    print("You Win")
else:
    print("Computer Wins!")



