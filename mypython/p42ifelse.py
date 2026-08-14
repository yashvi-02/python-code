temp=float(input("enter the temperature: "))
if temp < 0:
    print("Freezing Atmosphere")
elif temp >0 and temp < 10:
    print("Very cold atmosphere")
elif temp > 10 and temp < 20:
    print("cold atmosphere")
elif temp >20 and temp<30:
    print("normal atmosphere")
elif temp >30 and temp < 40:
    print("hot atmpsphere")
elif temp>40:
    print("very hot atmosphere")
else:
    print("other")
