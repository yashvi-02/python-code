def add():
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    add = num1+num2 
    print("addition: ", add)
def max2():
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    if num1 > num2:
        print(num1, "is maximum")
    else:
        print(num2, "is maximum")
def table():
    l = int(input("enter number: "))
    for i in range (1,11):
        print(l, "x", i, "=", l * i)
def max3():
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    num3 = int(input("enter a number: "))
    if num1 > num2 and num1 > num3:
        print(num1, "is greater")
    elif num2 > num1 and num2 > num3:
        print(num2, "is greater")
    elif num3 > num1 and num3 > num2:
        print(num3, "is greater")
    else:
        print("all numbers are equal")
def factorial():
    l= int(input("enter limit: "))
    for i in range (1,l):
        print(i, end="*")
    print()
def oddeven():
    l = int(input("enter a number: "))
    if l%2==0:
        print(l, "is even")
    else:
        print(l, "is odd")
def posneg():
    x = int(input("enter a number: "))
    if x >= 0:
        print("the number is positive.")
    else:
        print("the number is negative.")
def aroftri():
    base = int(input("enter base value: "))
    height = int(input("enter height value: "))
    area = 0.5 * base * height
    print("area of triangle:", area) 
def arofcir():
    r = int(input("enter r: ")) 
    area = 3.14 * r * r
    print("area of circle:", area)
print("press 1 for Addition")
print("press 2 to print Maximum of 2 numbers")
print("press 3 for Table")
print("press 4 to print Maximum of 3 numbers")
print("press 5 to print Factorial")
print("press 6 for Odd or Even")
print("press 7 for Positive or Negative")
print("press 8 for Area of Triangle")
print("press 9 for Area of Circle")
choice = int(input("Enter choice: "))
if choice == 1:
    add()
elif choice == 2:
    max2()
elif choice == 3:
    table()
elif choice == 4:
    max3()
elif choice == 5:
    factorial()
elif choice == 6:
    oddeven()
elif choice == 7:
    posneg()
elif choice == 8:
    aroftri()
elif choice == 9:
    arofcir()
else:
    print("Invalid choice")
