print("enter + for addition")
print("enter - for subtraction")
print("enter * for multiplication")
print("enter / for division")
op=input("enter option: ")
if op=="+":
    number1 = int(input("enter a number: "))
    number2 = int(input("enter a number: "))
    addition = number1+number2
    print("addition for 2 numbers is: ", addition)
elif op=="-":
    number1 = int(input("enter a number: "))
    number2 = int(input("enter a number: "))
    subtraction = number1-number2
    print("subtraction for 2 numbers is: ", subtraction)
elif op=="*":
    number1 = int(input("enter a number: "))
    number2 = int(input("enter a number: "))
    multiplication = number1*number2
    print("multiplication for 2 numbers is: ", multiplication)
elif op=="/":
    number1 = int(input("enter a number: "))
    number2 = int(input("enter a number: "))
    division = number1/number2
    print("division for 2 numbers is: ", division)
else:
    print("other")
