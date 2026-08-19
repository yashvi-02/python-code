def square():
    a = int(input("enter a number: "))
    square = a*a
    print("square of", a, "is: ", square)
def cube():
    b = int(input("enter a number: "))
    cube = b*b*b
    print("cube of", b, "is: ", cube)
print("press 1 for square")
print("press 2 for cube")
choice = int(input("enter choice: "))
if choice == 1:
    square()
elif choice == 2:
    cube()
else:
    print("invalid choice")
