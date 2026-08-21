india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city1 = str(input("enter first city: "))
city2 = str(input("enter second city: "))
if city1 and city2 == "mumbai" or city1 and city2 == "banglore" or city1 and city2 == "chennai" or city1 and city2 =="delhi" :
    print("they belong to same country")
else:
    print("they dont")
    if city1 and city2 == "lahore"or city1 and city2 == "karachi" or city1 and city2 == "islamabad":
        print("they belong to same country")
    else:
        print("they dont")
        if city1 and city2 == "dhaka"or city1 and city2 == "khulna" or city1 and city2 == "rangpur":
            print("they belong to same country")
        else:
            print("they dont")