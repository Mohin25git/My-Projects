while True:
    numInput = input("Enter a number: ")

    if numInput.lower() == "exit":
        print("Exiting program...")
        break

    num = int(numInput)

    if num > 0:
        print("The number is positive")

        if num % 2 == 0:
                print("even")
        else:
                print("odd")
    else:
        print("The number is not positive!!")

print()
