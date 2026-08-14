battery = int(input("enter battery percentage: "))
if battery>=80:
    print("battery is full")    
elif battery>=20 and battery<80:
    print("normal")
elif battery<20:
    print("battery is low")
else:
    print("error")