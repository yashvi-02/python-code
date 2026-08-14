print("enter pizza")
print("enter burger")
print("enter pasta")
print("enter garlic bread")
op=input("enter option: ").lower()
if op=="pizza":
    print("price of pizza is 230")
    qty = int(input("enter qty: "))
    print("your bill is: ", qty*230)
elif op=="burger" or op=="BURGER":
    print("price of burger is 340")
    qty = int(input("enter qty: "))
    print("your bill is: ", qty*340)
elif op=="pasta" or op=="PASTA":
    print("price of pasta is 300")
    qty = int(input("enter qty: "))
    print("your bill is: ", qty*300)
elif op=="garlic bread" or op=="GARLIC BREAD":
    print("price of garlic bread is 350")
    qty = int(input("enter qty: "))
    print("your bill is: ", qty*350)