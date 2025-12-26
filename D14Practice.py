#1 Print total and average marks of each student
record = [
    {"name":"Ram", "Math":44, "Science":45}, 
    {"name":"Shyam", "Math":50, "Science":55}
]

for student in record:
    total = student["Math"] + student["Science"]
    average = total / 2

    print(f"{student['name']}:- total marks: {total}, total average: {average}")

#2 Print if a student is approved or rejected according to their score. if score < 70 Rejected
grade = [
    {"name":"Mohin", "Math":71}, 
    {"name":"Sohan", "Math":70}, 
    {"name":"Rohan", "Math":69}, 
    {"name":"Mohan", "Math":68}
]

for students in grade:
    if student["Math"] >= 70:
        student["status"] = "Approved"
    else:
        student["status"] = "Rejected"

print(grade)

#3 Multiplication Table
num = int(input("Enter a number: "))

for m in range(1 ,11):
    print(f"{num} * {m} = {num * m}")

#4 Given list is [1,2,3,4] but expected output is [1,"a",2,4]
List = [1,2,3,4]

for j in range(len(List)):
    if List[j] == 3:
        List[j] = 'a'

print(List)

#5 Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists
items = [1,2,3,4,"a","b"]
integer = []
string = []

for t in items:
    if isinstance(t,int):
        integer.append(t)
    else:
        string.append(t)

print("these are integer:", integer)
print("these are string:", string)

#6 Python program that accepts a string and calculate the number of digits and letters
user_in = input("Enter a data: ")
NumCount = 0
StrCount = 0

for c in user_in:
    if c.isdigit():
        NumCount += 1
        
    elif c.isalpha():
        StrCount += 1
        
print("these are no of integers:", NumCount)
print("these are no of strings:", StrCount)

#7 Python program to check the validity of username and password input by users
min_character = 8 
userName = input("Enter a username: ")
password = input("Enter a password: ") 
# Initialize flags to track if password contains at least one letter and one number
has_letter = False
has_number = False 
# Loop through each character in the password to check its type
for c in password:
    if c.isalpha():
        has_letter = True # Found a letter, set the flag to True
    elif c.isdigit():
        has_number = True # Found a digit, set the flag to True

if has_letter and has_number and len(password) >= min_character:
    print("Access Granted!") 
else:
    print("Access Denied!")

#8 Python program to print multiplication tables from 1 to 8
for num in range(1, 9):
    print(f"Multiplication table for {num}: ")
    
    for n in range(1, 11):
        print(f"Product of: {num} * {n} = {num * n}")

    print() # Prints black line after each complete table for readability

#9 Given list is Lst = [1,2,3,4] but need to print 1 and 2 only
Lst = [1,2,3,4]
count = 0

for item in Lst:
    if count < 2:
        print(item, end=" ")
        count += 1

#10 Python program to calculate the sum of all odd number in given range.
startNo = int(input("Enter the starting range number: "))
endNo = int(input("Enter the ending range number: "))
total = 0

for num in range(startNo, endNo):
    if num % 2 != 0:
        total += num

print(total)

#11 python program to calculate the sum of all even number in given range.
startNo = int(input("Enter the starting range number: "))
endNo = int(input("Enter the ending range number: "))
total = 0

for num in range(startNo, endNo):
    if num % 2 == 0:
        total += num

print(total)

#12 python program to count the space of a given string.
string = input("Enter a string sentence: ")
count = 0

for s in string:
    if s == " ":
        count += 1

print(count)

#13 Given seq = [1,2,3,4] but expected output is [1,8,27,64].
seq = [1,2,3,4]
cube = []

for sq in seq:
        cube.append(sq ** 3)

print(cube)

#14 Reverse a string word = "Programming":
word = "Programming"
rev = ""

for r in word:
    rev = r + rev

print(rev)

#15 place a break statement in for loop so that it prints from 0-7 including 7. Given range(50)
for n in range(0, 50):
    if n == 8:
        break
    print(n)

#16 Write a for loop which print "Hello!," plus each name in the list. i.e.:"Hello!, Ram".
names = ["Ram","Arjun","Karn","Ashwadhama"]

for h in names:
    print(f"Hello!, {h}")

# Write a for loop that iterates through a string and prints every letter
Str = "Robotics"

for i in Str:
    print(i)
