'''
Create a Python program that greets the user with the message "Welcome to the
Haunted House". Then, ask the user whether they want to go "upstairs" or
"downstairs". If they choose "downstairs", print "Game Over". If they choose
"upstairs", ask if they want to "enter the room" or "stay outside". If they choose
"enter the room", print "Game Over". If they choose "stay outside", ask them to
choose between "ghost", "vampire", or "werewolf". If they choose "ghost" or
"vampire", print "Game Over". If they choose "werewolf", print "You Win
'''
print("Welcome to the Haunted House!")

stairs = input("Do you want to go upstairs or downstairs? ").lower()

if stairs == "downstairs":
    print("Game Over!")

elif stairs == "upstairs":
    choose = input("Do you want to enter the room or stay outside? ").lower()

    if choose == "enter the room":
        print("Game Over!")

    elif choose == "stay outside":
        monsters = input("Choose between ghost, vampire, or werewolf: ").lower()

        if monsters == "ghost" or monsters == "vampire":
            print("Game Over!")

        elif monsters == "werewolf":
            print("You Win!")

        else:
            print("Invalid choice!")

    else:
        print("Invalid choice!")

else:
    print("Invalid move!")

        


    

