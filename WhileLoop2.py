# WHILE LOOP EXAMPLES

# Example 1: Simple countdown
count = 5
print("\nExample 1: Countdown from 5 to 1")

# The loop continues as long as the condition (count > 0) is True
while count > 0:
    print(count)  # Print the current count
    count -= 1    # Reduce count by 1 each iteration
    # Loop will automatically stop when count <= 0

# Example 2: Loop until user enters 'stop'
print("\n Example 2: Loop until user types 'stop'")

user_input = ""  # Initialize variable to store user input

# Keep looping until the user types 'stop' (case-insensitive)
while user_input.lower() != "stop":
    user_input = input("Type 'stop' to end: ")  # Ask user for input
    print(f"You typed: {user_input}")          # Show what user typed

# Example 3: Increase battery until full
battery = 50
print("\n Example 3: Increase battery until full (100%)")

# Continue looping while battery is less than or equal to 100
while battery <= 100:
    print(f"Battery: {battery}%")  # Show current battery level
    battery += 10                  # Increase battery by 10 each iteration
    # Loop stops automatically when battery > 100

# Example 4: Loop with break condition
print("\n Example 4: Loop until a number greater than 50 appears")

import random  # Import random module to generate random numbers
number = 0

# Infinite loop: keeps running until we explicitly stop it
while True:
    number = random.randint(1, 100)  # Generate random number between 1 and 100
    print(f"Random number: {number}")
    if number > 50:
        print("Number greater than 50 found, stopping loop!")
        break  # Immediately exit the loop when condition is met

# Example 5: Loop with continue (skip certain steps)
print("\n Example 5: Print numbers 0-5 but skip 3")

i = 0  # Initialize counter

# Continue looping while i <= 5
while i <= 5:
    i += 1          # Increase counter by 1 at the start of each iteration
    if i == 3:
        continue   # Skip printing number 3 and go to next iteration
    print(f"Number: {i}")  # Print the current number if not skipped
    