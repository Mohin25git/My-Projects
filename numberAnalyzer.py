# Number analyzer
num = input("Enter a number: ")
reverse = num[::-1]
Digi_Count = 0
Digi_Sum = 0

for Digi in num:
    Digi_Count += 1
    Digi_Sum += int(Digi)

if num == reverse:
    print("The number is Palindrome!")
else:
    print(f"The reverse of the number is: {reverse}")

if int(num) % 2 == 0:
    print("The number is Even!")
else:
    print("The number is Odd!")

print(f"Total digits: {Digi_Count}")
print(f"Sum of digits: {Digi_Sum}")
