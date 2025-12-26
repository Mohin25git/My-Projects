while True:
    num1_input = input("Enter a number (or type 'exit' to quit): ")

    # Exit condition
    if num1_input.lower() == "exit":
        print("Exiting calculator... Goodbye!")
        break

    num2_input = input("Enter another number: ")

    # Convert both numbers safely
    try:
        num1 = int(num1_input)
        num2 = int(num2_input)
    except ValueError:
        print("Invalid number! Please enter valid integers.\n")
        continue

    # Ask for operation
    operation = input("Enter the operation (+ - * / **): ")

    # Perform the calculation
    if operation == "+":
        print("Result:", num1 + num2)

    elif operation == "-":
        print("Result:", num1 - num2)

    elif operation == "*":
        print("Result:", num1 * num2)

    elif operation == "/":
        # Check division-by-zero before dividing
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)

    elif operation == "**":
        print("Result:", num1 ** num2)

    else:
        print("Invalid operation!")

    print()  # spacing for readability
