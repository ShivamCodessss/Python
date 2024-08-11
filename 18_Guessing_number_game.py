# Number Guessing Game

import random

Play = input("Do you want to play ? ").lower()

if Play != "yes":
    print("See You Soon")
    quit()
else:
    print("Let's Start the Game:")

Computer_guess = random.randint(0,50)
Guesses = 0

while True:
    Guesses = Guesses + 1
    User_Input = input("Enter a number between 1 to 50")

    if User_Input >= "50":
        print("Enter number below 50: ")
        continue

    if User_Input.isdigit():
        User_Input = int(User_Input)
    else:
        print("Enter a number next time. ! " )
        continue

    if User_Input == Computer_guess:
        print("You Got It! ")
        break
    elif User_Input > Computer_guess:
        print("You were above the number! ")
    else:
        print("You were below the number! ")

print(f"you got it in {Guesses} Guesses!")