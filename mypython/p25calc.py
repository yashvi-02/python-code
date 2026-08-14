print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")
number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
op=int(input("enter your option: "))

if op==1:
    addition = number1+number2
    print("addition of numbers is: ", addition)
elif op==2:
    subtraction = number1-number2
    print("subtraction if the numbers is: ", subtraction)
elif op==3:
    multiplication = number1*number2
    print("multiplication of the numbers is: ", multiplication)
elif op==4:
    division = number1/number2
    print("division of the numbers is: ", division)


