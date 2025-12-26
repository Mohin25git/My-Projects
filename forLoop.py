# for loop Practice:

# Print name 10 times
for i in range(0, 10):
    print("Mohin")

# Print numbers from 1 to 20
for x in range(0, 20):
    print(x + 1)

# print even number up to 20
for y in range(2, 20, +2):
    print(y)

# print odd numbers up to 20
for z in range(1, 20, +2):
    print(z)

# Print each letter in a string
for w in "Robotics":
    print(w)

for ch in "PythonAI":
    print(ch)

# Print list in loop
for item in ["red","blue","green"]:
    print(item)

# Print numbers from 10 to 1 (reverse loop)
for n in range(10, 0, -1):
    print(n)

# Print numbers from 5 to 50, jumping by 5 each time
for j in range(5, 51, +5):
    print(j)

# Print the multiplication table of 7 using a for loop
for m in range(1, 11):
    print(m * 7)

# Count how many vowels are in "Artificial Intelligence"
Vowels = "aeiouAEIOU"
count = 0
for chr in "Artificial Intelligence":
    if chr in Vowels:
        count += 1
print(count)

# Find the sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100:", total)
