length = int(input("enter length in meters: "))
breadth = int(input("enter breadth in meters: "))
area = length*breadth
if length==breadth:
    print("this is not a rectangle, it is a square!")
else:
    print("area of rectangle: ", area)