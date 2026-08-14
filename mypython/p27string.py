print("enter s for square: ")
print("enter c for cube")
op=input("enter option: ")
if op=="s" or op=="S":
    number = int(input("enter a number"))
    square = number*number
    print("the square of the number is: ", square)
elif op=="c" or op=="C":
    number = int(input("enter a number"))
    cube = number*number*number
    print("the cube of the number is: ", cube)
    