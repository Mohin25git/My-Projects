# Write a program that takes three numbers as input and determines:
#If all three are equal then print "All numbers are equal"
#If exactly two are equal then print "Two numbers are equal"
#If all are different then print "All numbers are different"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 == num2 == num3:
    print("All numbers are equal")

elif num1 == num2 or num2 == num3 or num3 == num1:
    print("Two numbers are equal")
else:
    print("all are different")
