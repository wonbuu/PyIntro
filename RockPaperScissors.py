import random

letsPlay = True
rps = ["rock","paper","scissors"]
userChoice = ""

def shoot(usr):
    bot = random.choice(rps)
    print("I chose " + bot + ".")
    play = False
    if (usr in rps):
        if (bot == usr):
            print("Its a tie! Let's go again!")
            play = True
        elif (bot == "rock"):
            if (usr == "paper"):
                print("You win paper covers rock.")
            else:
                print("Good old trusty rock you lose.")
        elif (bot == "paper"):
            if (usr == "scissors"):
                print("You win scissor cutts paper.")
            else:
                print("HAHAHAHA you lost to paper!")
        elif (bot == "scissors"):
            if (usr == "rock"):
                print("You win rock smashes scissors")
            else:
                print("LOSER!")
    else:
        print("You chose wrong!\nEnter rock, paper, or scissors!")
        play = True
    return play

print("Lets play rock, paper, scissors!")

while letsPlay == True:
    userChoice = input("Enter your choice.\n")
    userChoice = userChoice.lower()
    letsPlay = shoot(userChoice)
