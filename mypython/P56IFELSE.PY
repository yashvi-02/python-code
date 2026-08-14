color = input("enter color: ").lower()
if color=="red":
    print("car is not allowed to go")
elif color=="yellow":
    print("car is allowed to go but with caution")
elif color=="green":
    print("car is allowed to go")
else:
    print("unrecognized signal")    