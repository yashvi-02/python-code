price = int(input("enter price: "))
if price>10000:
    discount =price-price*20/100
    print("marked price: ", discount)
elif price>7000 and price<=10000:
    discount = price-price*15/100
    print("marked price: ", discount)
elif price>=7000:
    discount = price-price*10/100
    print("marked price: ", discount)
else:
    print("no discount")


