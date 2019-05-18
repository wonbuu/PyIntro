
#getting informaiton from the user
location = input("Give me a location: ")
famousPerson = input("Give me the name of a famous person: ")
adjective1 = input("Give me an adjective: ")
sound = input("Give me a sound: ")
animal1 = input("give me an animal: ")
animal2 = input("give me another animal: ")
animal3 = input("give me yet another animal: ")
verb1 = input("Give me a verb: ")
typeOfPerson = input("Give me a type of person: ")
noun = input("Give me a noun: ")
verb2 = input("Give me another verb: ")
store = input("Give me the name of a store: ")
raceOfPeople = input("Give me a race of people: ")
alrightTerrible = ["alright", "terrible"]
choice = input("Choose alright or terrible")
if (choice in alrightTerrible):
    alrightTerrible = choice
else:
    alrightTerrible = alrightTerrible[0]
famousWoman = input("Give me the name of a famous woman: ")
verb3 = input("Give me yet another verb: ")
groupOfPeople = input("Give me a group of people: ")
place = input("Give me a place: ")
game = input("Give me a game: ")
setting = input("Give me a setting: ")
adverb = input("Give me an adverb: ")
accomplishment = input("Give me an accomplishment: ")
pluralNoun = input("Give me a plural noun: ")
unsucessfulAthlete =input("Give me the name of an unsucessful athlete.")
adjective2 = input("Give me another adjective: ")

#creating output
print("...")
print("Just waking up in the " + location + ", gotta thank " + famousPerson + ".")
print("I don't know, but today seems kinda " + adjective1 + ".")
print("No " + sound + "from the " + animal1 + ", no smog, and momma cooked a breakfast with no " + animal2 + ".")
print("I got my grub on, but I didn't " + animal3 + " out.")
print("Finally got a call from a girl I want to " + verb1 + ".")
print("Hooked it up later as I hit the door, thinking, Will I live to see another " + typeOfPerson + "?")
print("I gotta go \'cause I got me a " + noun + ", and if I hit the switch I can make the ass " + verb2 + ".")
print("Had to stop at a " + store + "; looking in the mirror, not a " + raceOfPeople + " in sight and everything is " + choice + ".")
print("I got a beep from " + famousWoman + " and she can " + verb3 + " all night.")
print("Calling up the " + groupOfPeople + " and I\'m askin y\'all,\"Which " + place + " are y\'all playing " + game + "?")
print("Get me on the " + setting + " and I\'m in trouble.")
print("Last week, " + adverb + "around and got a" + accomplishment + ".")
print("Freaking " + pluralNoun + " every way like " + unsucessfulAthlete + ".")
print("I can\'t believe today was a " + adjective2 + " day.")
