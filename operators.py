# Operators
a = 8
b = 10
c = 12
d = 14

# Airthmetic Operators
value_1 = a + b + c + d # Addition Operator
print(value_1)

value_2 = value_1 - d   # Substraction Operator
print(value_2)

value_3 = value_1 * a   # Multiplication Operator
print(value_3)

value_4 = value_1 / a   # Division Operator(float)
print(value_4)

value_5 = value_1 % b   # Modulus Operator(remainder)
print(value_5)

value_6 = value_1 ** a  # Exponential Operator(power)
print(value_6)

# Comparison Operators
e = 5
f = 5
print(e == f) # Equal-to Operator(prints true because 5=5)

g = 10
h = 8
print(g != h) # Not-Equal-to Operator(prints true because g isnt equal-to h)

i = 12
j = 9
print(i > j)  # Greater than Operator 


k = 16
l = 21
print(k < l)  # Less than Operator

m = 22
n = 21
print(m >= n) # Greater than Equal-to Operator

o = 69
p = 70
print(o <= p) # Less than Equal-to Operator

# Logical Operators
name = input("Enter your name: \n")
age = int(input("Enter your current age: ")) # Always add 'int' before input while asking a digit/number values
has_ID = input("Do you have ID? (yes/no): ").lower() == 'yes'

if age > 18 and has_ID: # AND operator(all must be True)
    print("Access Granted To Enter Exam hall!!")

else:
    print("Access Denied To Enter Exam hall!!")

# OR
career_Aim = input("Enter your career: ")
option_2 = input("Enter your second option: ")

if career_Aim == "Robotics" or option_2 == "Any":  # OR operator (one must be True)
    print("You are yourself!!")

# NOT
raining = True

if not raining: # NOT operator (Invert's result)
    print("Let's go outside! 🌤️")
else:
    print("Better stay inside ☔")

# Example 2:
tired = input("Are you tired? (yes/no): ").lower() == "yes"

if not tired:
    print("Time to study Python! 🐍")
else:
    print("Take a nap 😴") # Inverted Input If True it's False

# Assignment Operators
x = 10  # Basic assignment Store 10 in variable x
print("x =", x)  # Output: x = 10

# Add and Assign Operator(+=)
x = 5
x += 3  # Equivalent to x = x + 3
print("x after += 3:", x)

# Subtract and Assign Operator(-=)
x = 10
x -= 4  # Equivalent to x = x - 4
print("x after -= 4:", x)

# Multiply and Assign Operator(*=)
x = 7
x *= 2  # Equivalent to x = x * 2
print("x after *= 2:", x)

# Divide and Assign Operator(/=)
x = 20
x /= 4  # Equivalent to x = x / 4
print("x after /= 4:", x)

# Floor Division Operator           
x = 20
x //= 3  # Equivalent to x = x // 3
print("x after //= 3:", x)

# Logic of floor division:
# 17 ÷ 3 = 5.666
# Floor division → drop the decimal → 5
# Store back in x → x = 5

# Modulus and Assign Operator(%=)
x = 17
x %= 5  # Equivalent to x = x % 5(remainder)
print("x after %= 5:", x)

# Exponent and Assign Operator(**=)
x = 3
x **= 2  # Equivalent to x = x ** 2(power)
print("x after **= 2:", x)

#Bitwise Operators and Assign
# &=, |=, ^=, <<=, >>=
x = 10   # 1010 in binary
x &= 6   # 1010 & 0110 = 0010 where, there must be 1 and 1 to get 1
print("x after &= 6:", x)









