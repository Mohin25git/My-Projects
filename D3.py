def logs():
    '''
    hello!
    this is an instruction
    to doc-string execution
    testing 123
    '''
logs()
print(logs.__doc__)

# Membership Operator
studentName = ["Mohin", "Elon", "Tony", "Jeff"]
name = input("Enter a student's name: ")
# print("Mohin" in studentName) # Output: True
# print("Manish" in studentName) # Output: False

if name in studentName:
    print("True")
else:
    print("False")

if name not in studentName:
    print("False")

else:
    print("True")

# Identity operators
num_1 = 20
num_2 = 22
print(id(num_1))
print(id(num_2))
print(num_1 is num_2)

#Bitwise Operators and Assign
# &=, |=, ^=, <<=, >>=
x = 10   # 1010 in binary
x &= 6   # 1010 & 0110 = 0010 where, there must be 1 and 1 to get 1
print("x after &= 6:", x)

#self class
# do commit to git
