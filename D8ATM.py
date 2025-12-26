pin = 123
balance = 50000

while True:
    card = input("Do you have a card? (yes/no/exit): ").lower()

    if card == "exit":
        print("Exiting ATM... Goodbye!")
        break

    if card != "yes":
        print("You need a card to use the ATM.")
        continue   # restart loop

    entered_pin = int(input("Enter your PIN: "))

    if entered_pin != pin:
        print("Wrong PIN!\n")
        continue   # restart loop

    # Logged in successfully
    while True:
        print("\n--- ATM MENU ---")
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit to Main Menu")
        print("4. Exit ATM")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawal successful! Remaining balance = {balance}")
            else:
                print("Insufficient balance!")

        elif choice == "2":
            print(f"Your balance is: {balance}")

        elif choice == "3":
            print("Returning to main screen...\n")
            break   # go back to card check loop

        elif choice == "4":
            print("Exiting ATM... Goodbye!")
            exit()

        else:
            print("Invalid option!")
