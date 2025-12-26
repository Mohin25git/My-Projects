'''In a smart building lift system, the lift is currently at floor 5. A person presses
floor 3. Write a program to decide and display whether the lift should go up, go
down, or stay at current floor'''

current_floor = 5

user_input = int(input("Enter the floor you want to go to: "))
floors = [1, 2, 3, 4, 5, 6, 7, 8]

if user_input in floors:
    
    if user_input > current_floor:
       print("lift goes upwards")

    elif user_input < current_floor:
       print("lift goes downwards")

else:
    print("invalid floor")

