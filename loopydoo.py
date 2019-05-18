#using a list
animalList = ['bear', 'pig', 'man']
for i in animalList:
    print(i)
print(i)
#using a range
for j in range(0, len(animalList)):
    print(j)
    print(animalList[j])
print(j)
#conditional
a = True
b = True
if a and b:
    print('yes')
else:
    print('no')

pepsi = 'bepis'
if pepsi not in animalList:
    animalList.append(pepsi)
