# While loop Practice
'''
A while loop is used when:
You dont know in advance how many times something should repeat

Instead of saying:
“Do this 10 or '----' times”
We are saying:
“Keep doing this until a condition becomes False”
'''
# Write a while loop that prints numbers from 1 to 10
num = 1

while num <= 10:
    print(num)
    num += 1

# Reverse print 10 to 1
num = 10

while num >= 1:
    print(num)
    num -= 1

# Print even numbers from 2 to 20
num = 2

while num <= 20:
    print(num)
    num += 2

# Print "Hello Python" 5 times using a while loop
count = 1

while count <= 5:
    print("Hello Python")
    count += 1

# Calculate the sum of numbers from 1 to 100
count = 1
sum = 0

while count <= 100:
    sum = count + sum
    count += 1
print(sum)

# Multiplication table
num = int(input("Enter a number: "))
count = 1

while count <= 10:
    print(f"{num} x {count} = {num * count}")
    count += 1

# Password checker
password = input("enter your password: ")

while password != "admin@123":
    password = input("Incorrect password! try again: ")

print("Access Granted!")

# COUNTING DIGITS
digi = int(input("Enter a digit: "))
# This variable will count how many digits the number has
count = 0
# Loop runs as long as there are digits left in the number
while digi > 0:
    # Remove the last digit by integer division
    digi = digi // 10
    # Each time we remove a digit, increase the count
    count += 1
# After the loop ends, 'count' holds the total number of digits
print("Number of digits =", count)

# PROGRAM 2: REVERSE A NUMBER
num = int(input("Enter a number: "))
# This variable will store the reversed number
reverse = 0
# Loop until all digits of the number are processed
while num > 0:
    # Extract the last digit of the number
    digit = num % 10
    # Shift existing digits left and add the new digit
    reverse = reverse * 10 + digit
    # Remove the last digit from the original number
    num = num // 10
# After the loop, 'reverse' contains the reversed number
print("Reversed number =", reverse)

# PROGRAM 3: SUM OF DIGITS
num = int(input("Enter a digit: "))
# This variable accumulates the sum of digits
total = 0
# Loop until all digits are added
while num > 0:
    # Get the last digit
    digit = num % 10
    # Add the digit to the running total
    total = total + digit
    # Remove the last digit from the number
    num = num // 10
# After the loop, 'total' stores the sum of all digits
print("Sum of digits =", total)
