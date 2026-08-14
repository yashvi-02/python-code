download = int(input("enter download speed in mbps: "))
if download<10:
    print("your download speed is slow")
elif download>=10 and download<50: 
    print("your download speed is average")
elif download>=50 and download<100:
    print("your download speed is fast")
else:
    print("your download speed is very fast")