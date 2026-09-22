marks = {
    "ram": 33,
    "rahul": 45,
    "manav": 30,
    "jayul": 34,
    "meena": 29,
    "siddhi": 48
}
key = input("enter value to search: ")
for values in marks.items():
    if key in values:
        print("value found")
        break
else:
    print("value not found")
