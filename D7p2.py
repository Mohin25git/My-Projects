# calculator in class
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

operators = input("Enter the operation to perform(+, -, *, **): ")

operator_value = {"+": num1 + num2, "-": num1 - num2, "*": num1 * num2, "**": num2 ** num2}

if (operators in operator_value):
    result = operator_value[operators]
    print(result)

elif operators == "/":
    if num2 == 0:
       print("Cannot divide by zero!")

    else:
       print(num1 / num2)

else:
    print("Invalid operator!")

