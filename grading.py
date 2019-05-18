#accepting the input from the user
grade = int(input("What grade did you get?"))

#building the results
print('You get ')

if (grade > 100):
    print("EXPELLED FOR CHEATING")
elif (grade > 89):
    print("A")
elif (grade > 79):
    print("B")
elif (grade > 69):
    print("C")
elif (grade > 59):
    print("D")
else:
    print("F")
