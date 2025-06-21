
print ("Hello, welcome to Alpha's budget calculator")

income = float(input("Enter your total monthly income: £"))

categoryNumber = int(input("How many expense categories do you want to enter? "))

def ordinal(n):
    if 11 <= n % 100 <= 13:
        suffix = "th"
    else:
        last_digit = n % 10
        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"

    return str(n) + suffix

expenses = {}

for i in range(categoryNumber):
    category_name = input(f"What is the {ordinal(i+1)} category name?  ")
    amount = float(input(f"How much do you spend on {category_name}? £"))
    expenses[category_name] = amount

total_expenses = sum(expenses.values())

remaining_money = income - total_expenses

print (f"Income: £{income:.2f}")
print (f"Total Expenses: £{total_expenses:.2f}")
print (f"Remaining Money: £{remaining_money:.2f}")
