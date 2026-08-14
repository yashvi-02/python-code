distance = int(input("enter distance in km: "))
if distance==5:
    print("the fare is 20 rupees per km for first 5km")
elif distance>5 and distance<=10:
    print("the fare is 20 rupees for first 5km and 10 rupees for next 5km")
else:
    print("the fare is 20 rupees for first 5km and 10 rupees for next 5km")