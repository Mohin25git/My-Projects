#            FRIENDLIST MANAGER

# A fun and simple Python program that lets you:
# Manage your list of friends (List)
# Store hobbies and details (Dictionary)
# Keep track of best friends (Tuple)
# It uses loops, conditionals, and user inputs

# Create an initial list of friends
# Lists are flexible — you can add or remove names anytime(mutable)
initial_list = ["Tony", "Elon", "Boston", "Mohin"]

# Create a dictionary mapping friends → their hobbies
# Dictionaries store key-value pairs.
# Example: "Tony" (key) → "Philanthropist" (value)
friendsAim = {
    "Tony": "Philanthropist",
    "Elon": "Multi-Billionaire",
    "Boston": "Machineries",
    "Mohin": "Robotics"
}

# Define your unchangeable best friends using a tuple
# Tuples are immutable — once created, you can’t edit them
bestfriends = ("Sumala", "Kumala")

# Display the welcome message and available commands
print("Welcome My New Friends!!")
print("Type: add | remove | view | best | exit")
print("---------------------------------------")

# Main control loop — runs forever until 'exit' is typed
# This makes the program interactive, always waiting for your next move.
while True:
    # Take user input and normalize it
    # .strip() removes extra spaces; .lower() ensures consistency
    actionTaken = input("\nWhat action would you like to take? ").strip().lower()

    # Add a new friend to the list and dictionary
    if actionTaken == "add":
        newName = input("Enter your name: ").title().strip() #.title() converts the First letter into Uppercase and Rest to lower
        newHobby = input(f"What does {newName} love to do? ").strip()

        # Add the new friend to both list and dictionary
        initial_list.append(newName)
        friendsAim[newName] = newHobby

        print(f"✅ {newName} added with hobby: {newHobby}")

    # Remove an existing friend from both list and dictionary
    elif actionTaken == "remove":
        newName = input("Enter a name to be removed: ").title().strip()

        # Check if the name exists before removing (to avoid errors)
        if newName in initial_list:
            initial_list.remove(newName)
            friendsAim.pop(newName, None) # .pop() removes items, and None prevents unwanted errors when the item isn’t found
            print(f"🗑️ {newName} has been removed successfully!!")
        else: 
            print("⚠️ The name doesn’t exist in the list!!")

    # View all current friends and their hobbies
    elif actionTaken == "view":
        print("\n--- 🧑‍🤝‍🧑 YOUR FRIEND LIST ---")

        # Loop through the list and fetch each friend’s hobby from dictionary
        # .get() prevents KeyError — returns “Unknown” if name not found
        for newName in initial_list:
            newHobby = friendsAim.get(newName, "Unknown")
            print(f"{newName} loves {newHobby}")
   
    # Display best friends (Tuple)
    elif actionTaken == "best":
        # Tuples are displayed as is — showing the special BFFs are Unchangable(im-mutable)
        print(f"\n💎 BFF Forever: {bestfriends}")

    # Exit the program safely
    elif actionTaken == "exit":
        print("\n👋 Exiting FriendList Manager!!!")
        break  # Breaks out of the infinite loop, ending the program

    # Handle any unknown command
    else:
        print("Unknown command entered! Try again using: add | remove | view | best | exit")

# With AI