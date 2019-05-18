import random

magic = ["You will be eaten by howler monkeys", "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
running = True

while (running):
    input("Please ask a Yes/No question:\n")
    print(random.choice(magic))
    shakeAgain = input("Would you like to shake the ball again again?\n")
    if (shakeAgain.lower() != "yes"):
        running = False
print("Thanks for playing!")
