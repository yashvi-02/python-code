ch=input("Enter char: ")
if ch.isupper():
    print(ch.lower())
elif ch.islower():
    print(ch.upper())
else:
    print("other")