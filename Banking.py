Users = {
    "Mohin": {"balance": 1050000, "history": []},
    "Rohan": {"balance": 105005, "history": []},
    "Tony": {"balance": 150050000, "history": []},
    "Elon": {"balance": 1500500000, "history": []},
    "Jeff": {"balance": 1200020000, "history": []}
}

menu_option = ["Deposit", "Withdraw", "Transfer", "History", "Exit"]

user_choice = input("Enter the account-holder name: ").lower()

user_input = None
for name in Users:
    if name.lower() == user_choice:
        user_input = name
        break

if user_input is None:
    print("User doesn't exist!")
    exit()

print("Menu option:")
for i, option in enumerate(menu_option, 1):
    print(f"{i}. {option}")

choice = input("Enter your choice: ").lower()

if choice == "deposit":
    amount = int(input("Enter amount to deposit: "))
    Users[user_input]["balance"] += amount
    Users[user_input]["history"].append(f"Deposit: {amount}")
    print("Successfully Deposited!")

elif choice == "withdraw":
    amount = int(input("Enter amount to withdraw: "))
    if amount <= Users[user_input]["balance"]:
        Users[user_input]["balance"] -= amount
        Users[user_input]["history"].append(f"Withdraw: {amount}")
        print("Successfully Withdrawn!")
    else:
        print("Insufficient balance!")

elif choice == "transfer":
    receiver_input = input("Enter receiver's name: ").lower()
    receiver = None

    for name in Users:
        if name.lower() == receiver_input:
            receiver = name
            break

    if receiver is None:
        print("Invalid User!")
    else:
        amount = int(input("Enter amount to transfer: "))
        if amount <= Users[user_input]["balance"]:
            Users[user_input]["balance"] -= amount
            Users[receiver]["balance"] += amount
            Users[user_input]["history"].append(f"Transfer to {receiver}: {amount}")
            print("Successfully Transferred!")
        else:
            print("Insufficient balance!")

elif choice == "history":
    print("Transaction history:")
    for h in Users[user_input]["history"]:
        print(h)

elif choice == "exit":
    print("Exiting banking app!")
    exit()

else:
    print("Invalid Choice!")

print(f"Your current balance is {Users[user_input]['balance']}")
