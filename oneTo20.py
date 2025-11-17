# Counting even numbers from 1 to 20 using loops and conditionals 
for number in range(1, 21): # Loop through numbers 1 to 20; 21 because count starts from 0
    if number % 2 == 0:     # Checking if divisible by 2 (even number)
        print(number)       # Printing only the even ones

# Asking user for range of number
start_range = int(input("Enter the starting range number: "))
end_range = int(input("Enter the ending range number: "))

print(f"\nEven Numbers between {start_range} and {end_range} are:")

# Looping through the range
for number in range(start_range, end_range +1): # +1 so that last number is included
    
    # Conditional check "Checking if divisible by 2 (even number)"
    if number % 2 == 0:
        print(number)
