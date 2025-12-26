'''
Scenario:
Your robot has a temperature sensor. You want to write a program that:
Takes the robot’s temperature as input (in °C)
Checks the temperature
Prints the correct action your robot should take

Conditions:
If temperature > 50°C → print "Overheating! Activate cooling system."

If temperature between 30°C and 50°C (inclusive) → print "Temperature normal."

If temperature < 30°C → print "Too cold! Activating heat regulator."
Task:
Write a Python program using input(), if-elif-else, and correct comparison operators.
'''
temp = int(input("Enter the temperature in °C: "))

if temp >= 50:
    print("Overheating! Activate cooling system.")
elif temp >= 30 and temp <= 50:
    print("Temperature Normal!")
else:
    print("Too cold! Activating heat regulator.")
