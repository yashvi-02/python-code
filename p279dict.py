my_expenses = {
    "Clothes": 1100,
    "Shoes": 1000,
    "Watch": 900,
    "Mobile Recharge": 699,
    "Petrol": 1980
}

wife_expenses = {
    "Mobile Recharge": 799,
    "DTH recharge": 999,
    "Clothes": 2310,
    "Makeup": 3670,
    "Shoes": 999
}
my_total_expenses = sum(my_expenses.values())
wife_total_expenses = sum(wife_expenses.values())

print(f"My total expenses: ${my_total_expenses}")
print(f"Wife's total expenses: ${wife_total_expenses}")

if my_total_expenses > wife_total_expenses:
    print("I am spending more.")
elif wife_total_expenses > my_total_expenses:
    print("My wife is spending more.")
else:
    print("We are spending same.")

my_expensive_item = max(my_expenses, key=my_expenses.get)
wife_expensive_item = max(wife_expenses, key=wife_expenses.get)

print(f"The most expensive item I bought is {my_expensive_item} with an amount of ${my_expenses[my_expensive_item]}.")
print(f"The most expensive item my wife bought is {wife_expensive_item} with an amount of ${wife_expenses[wife_expensive_item]}.")