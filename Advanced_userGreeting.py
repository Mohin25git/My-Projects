# ROBOTICS LAB GREETING PROGRAM

# Importing the datetime module to handle time
from datetime import datetime

# Asking the User for their name
name = input("Enter your name, Commander: ")

# Getting current time
now = datetime.now()

# Extracting hour in 24-hour format
hour = now.hour

# Converting to 12-hour format using strftime
current_time = now.strftime("%I:%M %p")  # %I = hours, %M = minutes, %p = AM/PM

# Choosing a greeting based on the hour
if 5 <= hour < 12:
    greeting = "Good morning"
elif 12 <= hour < 18:
    greeting = "Good afternoon"
elif 18 <= hour < 22:
    greeting = "Good evening"
else:
    greeting = "Burning the midnight oil, huh"

# Displaying the greeting and current time
print(f"\n{greeting}, {name}! The current lab time is {current_time}")
print("Welcome to the Robotics Lab")

# Adding some cool loading lines
print("\nInitializing systems...")
print("Powering servo motors...")
print("Calibrating sensors...")
print(f"All set, Commander {name}! Your Bots Army awaits orders!!!!")

# Done by AI