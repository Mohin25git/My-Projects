password = input("Enter your password: ")
# Default Flags
has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
        
if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Strong password!")

elif not has_upper:
    print("Password must have atleast one uppercase letter!")

elif not has_lower:
    print("Password must contain atleast one lowercase letter!")

elif not has_digit:
    print("Password must contain atleast one digit!")

else:
    print("Access Denied! create stronger password!")
