import string
import random

passStr = ''
poolStr = string.ascii_letters + string.digits + string.punctuation
passLength = int(input("How long should your password be?\n:"))
probLow = int(input("What is the percentage of lower case characters\nEXAMPLE type 30 for 30%\n:"))
probUp = int(input("What is the percentage of upper case characters\nEXAMPLE type 30 for 30%\n:"))
probDig = int(input("What is the percentage of digit characters\nEXAMPLE type 30 for 30%\n:"))
probPunct = int(input("What is the percentage of punctuation characters\nEXAMPLE type 30 for 30%\n:"))

#accounting for people that don't know that percentage is up to 100% and no more
probTot = probLow + probUp + probDig + probPunct

#get the number of different characters in they correct type
numLow = ((probLow / probTot)  * passLength) // 1
numUp = ((probUp / probTot) * passLength) // 1
numDig = ((probDig / probTot) * passLength) // 1
numPunct = ((probPunct / probTot) * passLength) // 1

#add on what is need to fill length of password
selected = numLow + numUp + numDig + numPunct
if selected != passLength:
    numLow = numLow + (passLength - selected)

#create lists of characters for randomly choosing
Low = []
Up = []
Dig = []
Punct = []

while len(Low) < numLow:
    Low.append(random.choice(string.ascii_lowercase))
while len(Up) < numUp:
    Up.append(random.choice(string.ascii_uppercase))
while len(Dig) < numDig:
    Dig.append(random.choice(string.digits))
while len(Punct) < numPunct:
    Punct.append(random.choice(string.punctuation))

#construct the password
passLst = [Low, Up, Dig, Punct]

i = 0

while (i < passLength):
    choice = random.choice(passLst)
    if len(choice) == 0:
        passLst.pop(passLst.index(choice))
    else:
        passStr = passStr + choice.pop()
        i = i + 1
print(passStr)
