# VARIABLES

# String variable: stores alphabets/names
name = "Mohin"  
print(name)  # Output: Mohin

# Integer variable: stores number/digits
age = 22  
print(age)  # Output: 22

# Mutable dataset (List): stores robot types
robo_list = ["pathfinder Rover", "Humanoid", "Quadropped"]  
print(robo_list)  # Output: ['pathfinder Rover', 'Humanoid', 'Quadropped']

# Immutable dataset (Tuple): stores coordinates
roboTuples = (20, 30, 40)  
print(roboTuples)  # Output: (20, 30, 40)

# Dictionary: stores key-value pairs
Dictionary = {"name": "Mohin", "age": 22, "college": "Softwarica"}  
print(Dictionary)  # Output: {'name': 'Mohin', 'age': 22, 'college': 'Softwarica'}

# Accessing a specific value in the dictionary
print(Dictionary["college"])  # Output: Softwarica

# Boolean variables
is_robot_active = True
print(is_robot_active)  # Output: True

has_college_degree = False
print(has_college_degree)  # Output: False

# IF-ELSE STATEMENTS

# Battery percentage of the robot
batteryPercent = 50

if batteryPercent > 80:
    print("On full capacity")
elif 25 < batteryPercent <= 80:
    print("Half to moderate capacity")
else:
    print("Battery running out of capacity")

# FOR LOOP

# Example 1: Iterating through a list of robot types
print("\n For Loop Example:")

for robot in robo_list:
    # Print the current robot type
    print(f"Robot type: {robot}")  # e.g., Robot type: Pathfinder Rover

# Example 2: Iterating through a sequence of numbers using range()
print("\n Counting with for loop:")

for i in range(5):
    # i starts from 0, so we add 1 for human-friendly counting
    print(f"Step {i+1}")  # Prints Step 1, Step 2, ..., Step 5

# WHILE LOOP

print("\n While Loop Example")

# Initialize battery percentage
batteryPercent = 50  

while batteryPercent > 0:
    # Print the current battery level
    print(f"Battery at {batteryPercent}%")
    
    # Reduce battery by 10 in each loop iteration
    batteryPercent -= 10  

print("Battery fully drained!")

# FILE MANAGEMENT

# Write to a file named "Intro.txt"
with open("Intro.txt", "w") as f:
    # Write a simple line of text
    f.write("My name is Mohin Man Shakya")
    # File automatically closes after this block

# Read and print content from a file named "Motive.txt"
with open("Motive.txt", "r") as f:
    # Read the file's content and print it
    print(f.read())

# Self practice