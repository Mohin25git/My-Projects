import dis

# Example 1: Simple Add Function
print("add function begins:\n")

# Define a simple function to add two numbers
def add(a, b):
    return a + b  # Returns the sum of a and b

dis.dis(add) # Disassemble the 'add' function to see its bytecode

print("add function complete!!\n")

# Example 2: If-Else Check Function
print("loop check function begins:\n")

# Define a function that checks if x > 5
def check(x):
    if x > 5:
        return "Big"   # Returns "Big" if x is greater than 5
    else:
        return "Small" # Returns "Small" if x is 5 or less

dis.dis(check) # Disassemble the 'check' function to see its bytecode

print("loop check function complete!!")

# self Class