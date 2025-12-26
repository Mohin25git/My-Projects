'''
Write a Python script using a for loop and the range() function 
to iterate through the numbers from 1 up to and includin Inside 
the loop, check if each number is even or odd, and then print 
the result in the format: "Number X is [even/odd] 
Output:
Number 1 is odd.
Number 2 is even.
Number 3 is odd.
Number 4 is even.
Number 5 is odd.
'''
for X in range(1, 6):

    if X % 2 == 0:
        print(f"Number {X} is Even")
    else:
        print(f"Number {X} is Odd")
