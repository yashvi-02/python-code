print("PRess 1 for square")
print("Press 2 for cube")
op=int(input("Enter option =>"))

if op==1:
    number = int(input("enter a number: "))
    square = number*number 
    print("Square of the number: ", square)

elif op==2:
    number = int(input("enter a number: "))
    cube = number*number*number
    print("cube of the number: ", cube)
