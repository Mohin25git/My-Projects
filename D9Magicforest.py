'''
Create a Python program that greets the user with the message "Welcome to the
Magic Forest". Then, ask the user whether they want to go "north" or "south". If
they choose "south", print "Game Over". If they choose "north", ask if they want to
"cross the river" or "follow the path". If they choose "cross the river", print "Game
Over". If they choose "follow the path", ask them to choose between "fairy", "ogre",
or "elf". If they choose "ogre" or "fairy", print "Game Over". If they choose "elf",
print "You Win"
'''
print("Welcome to the Magic Forest")

direction = input("Enter the direction you want to go (north/south): ").lower()

if direction == "south":
    print("Game Over!")

elif direction == "north":
    choice = input("Do you want to 'cross the river' or 'follow the path'? ").lower()

    if choice == "cross the river":
        print("Game Over!")

    elif choice == "follow the path":
        creature = input("Choose between 'fairy', 'ogre', or 'elf': ").lower()

        if creature == "fairy" or creature == "ogre":
            print("Game Over!")

        elif creature == "elf":
            print("You Win!")
        else:
            print("Invalid choice!")

    else:
        print("Invalid choice!")

else:
    print("Invalid direction!")
