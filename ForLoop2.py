# FOR LOOP EXAMPLES

print("Loop through list of robot names: ")

# Create a list of robot types
robo_names = ["Pathfinder Rover", "Humanoid", "Quadruped", "Aerial Drone"]

print("Example 1: Loop through the list\n")

# 'for' loop iterates over each item in the list one by one
for robot in robo_names:
    # 'robot' is a temporary variable holding the current list item
    print(f"robo_names: {robot}") # Prints the current robot name

# EXAMPLE 2: Loop through numbers using range()
print("Example 2: looping throught range function: 1 to 5")

# range(1,6) generates numbers starting from 1 upto 6 but, doesnt include 6 due to values starting from 0
for i in range(1, 6): # i is the Loop counter that changes in each iterations
    print(f"step{i}") # Prints Step 1, Step 2, ..., Step 5

# Greet using f-string AKA formatted string lateral
name = "Mohin"
print(f"Hello {name}, welcome to the robotics lab!")

# Greet example 2: Ask the user to enter their name
name = input("Enter your name: ")
print(f"Hello {name}, welcome to the robotics lab of Mohin M Shakya!")

# Self and AI