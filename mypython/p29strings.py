print("enter p for pizza")
print("enter b for burger")
print("enter pa for pasta")
print("enter g for garlic bread")
op=input("enter option: ")
if op=="p" or op=="P":
    print("price of pizza is 230")
    qty = int(input("enter qty: "))
    print("your bill is: ", qty*230)
elif op=="b" or op=="B":
    print("price of burger is 340")
    qty = int(input("enter qty: "))
    print("your bill is: ", qty*340)
elif op=="pa" or op=="PA":
    print("price of pasta is 300")
    qty = int(input("enter qty: "))
    print("your bill is: ", qty*300)
elif op=="g" or op=="G":
    print("price of garlic bread is 350")
    qty = int(input("enter qty: "))
    print("your bill is: ", qty*350)