print("Welcome to Computer Quiz! ")

User_Input = input("Do You Want To Play: ")

if User_Input.lower() != "yes":
    quit()
else:
    print("Let's Start!")

score = 0

Quest_1 = input("What does CPU stand for: ")
if(Quest_1.lower() == "centeral processing unit"):
    print("Correct!")
    score =+ 1
else:
    print("Incorrect!")

Quest_1 = input("What does GPU stand for: ")
if(Quest_1.lower() == "graphic processing unit"):
    print("Correct!")
    score =+ 1
else:
    print("Incorrect!")

Quest_1 = input("What does PSU stand for: ")
if(Quest_1.lower() == "power supply unit"):
    print("Correct!")
    score =+ 1
else:
    print("Incorrect!")

Quest_1 = input("What does RAM stand for: ")
if(Quest_1.lower() == "random access memory"):
    print("Correct!")
    score =+ 1
else:
    print("Incorrect!")


print(f"You Got {score} Right Answers")
print("You Got", ((score / 4 ) * 100))