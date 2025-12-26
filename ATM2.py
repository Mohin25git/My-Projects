initial_balance = 25050000
daily_limit = 25000
amt_withdrawn = 0

amount = int(input("Enter the amount to withdraw: "))

rem_limit = daily_limit - amt_withdrawn

if amount <= 0:
    print("Invalid! please enter a positive number.")

elif amount > initial_balance:
    print("Invalid amount! cannot withdraw more than current amount.")

elif amount > rem_limit:
    print("Maximum withdraw limit reached!")

else:
    amt_withdrawn += amount
    initial_balance -= amount
    print("Sucessfully withdrawed!")
    print(f"Remaining balance: {initial_balance}")
    print(f"Remaining withdraw limit: {daily_limit - amt_withdrawn}")
