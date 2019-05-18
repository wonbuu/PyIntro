import random
num = random.randint(1, 10)
winner = False
guesses = 0
dif = 0
last = 0
while True:
    usr = int(input("What number am I thinkiing of?\n:"))
    guesses = guesses + 1

    if usr < num:
        print("Too low!")
    elif usr > num:
        print("Too high")
    elif usr == num:
        winner = True
        break

    dif = abs(num - usr)
    if guesses == 1:
        last = dif
    if (dif > last):
        print("You can do better")
    else
        print("You are doing your best")
    last = dif
    
if winner:
    print("You win!")
    print("You guessed this many times: " + guesses)
else:
    print("You lose!")
print("I was thinking of " + str(num))
