def addition():
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    add = num1+num2 
    print("addition: ", add)
def subtraction():
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    sub = num1-num2 
    print("subtraction: ", sub)
def multiplication():
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    mul = num1*num2 
    print("multiplication: ", mul)
def division():
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    div = num1/num2 
    print("division: ", div)
print("press 1 for Addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")
choice = int(input("Enter choice: "))
if choice == 1:
    addition()
if choice == 2:
    subtraction()
if choice == 3:
    multiplication()
if choice == 4:
    division()
else:
    print("Invalid choice")

