monthly_expenses = {
    "January": 2200,
    "February": 2350,
    "March": 2600,
    "April": 2130,
    "May": 2190,
    "June": 1980,
    "July": 2400,
    "August": 2250,
    "September": 2100,
    "October": 2400,
    "November": 2150,
    "December": 2500
}

print("1. In February, how many dollars did you spend extra compared to January?")
february_expense = monthly_expenses["February"]
january_expense = monthly_expenses["January"]
extra_spent = february_expense - january_expense
print(f"In February, you spent ${extra_spent} extra compared to January.")

print("2. Calculate your total expenses for the first quarter (January to March) of the year.")
first_quarter_expenses = sum(monthly_expenses[month] for month in ["January", "February", "March"])    
print(f"Total expenses for the first quarter: ${first_quarter_expenses}")

print("3. Check if you spent exactly 2400 dollars in any month.")
if 2400 in monthly_expenses.values():
        print("Yes, you spent exactly $2400 in at least one month.")
else:
        print("No, you did not spend exactly $2400 in any month.")

print("4. Modify the expense for June (2080 dollars) to your monthly expenses.")
monthly_expenses["June"] = 2080
print("Expense for June has been modified.")
for month, expense in monthly_expenses.items():
    print(f"{month}: ${expense}")

print("5. You returned an item that you bought in April and received a refund of 200 dollars.")
monthly_expenses["April"] -= 200
print("Refund processed for April.")
print("Updated expenses for April:")
for month, expense in monthly_expenses.items():
    print(f"{month}: ${expense}")

print("6. Determine which month had the highest expense and print the month and the amount.")
highest_expense_month = max(monthly_expenses, key=monthly_expenses.get)
highest_expense_amount = monthly_expenses[highest_expense_month]
print(f"The month with the highest expense is {highest_expense_month} with an amount of ${highest_expense_amount}.")

print("7. Calculate the average monthly expense for the first half of the year (January to June).")
first_half_expenses = sum(monthly_expenses[month] for month in ["January", "February", "March", "April", "May", "June"])
average_first_half_expense = first_half_expenses / 6
print(f"The average monthly expense for the first half of the year is ${average_first_half_expense:.2f}.")

print("8. Find the month with the lowest expense and print the month and the amount.")
lowest_expense_month = min(monthly_expenses, key=monthly_expenses.get)
lowest_expense_amount = monthly_expenses[lowest_expense_month]
print(f"The month with the lowest expense is {lowest_expense_month} with an amount of ${lowest_expense_amount}.")