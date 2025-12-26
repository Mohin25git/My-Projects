"""
Create a weight conversion program that:
 Asks the user what their Earth weight is (as a float).
 Asks the user for a planet number (as an int).
Then, use an if/elif/else statement to calculate the user's weight on the
destination planet.
To calculate the user's weight: destination weight=Earth weight × relative gravity
Number Planet   Relative Gravity
1      Mercury    0.38
2      Venus      0.91
3      Mars       0.38
4      Jupiter    2.53
5      Saturn     1.07
6      Uranus     0.89
7      Neptune    1.14
If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid
planet number'.
"""
weight = float(input("Enter the earths weight: "))
number = int(input("Enter the planets number(1. mercury, 2. venus, 3. mars, 4. jupiter, 5. saturn, 6. uranus, 7. neptune): "))

if number == 1:
    newWeight = weight * 0.38
    print(newWeight)

elif number == 2:
    newWeight = weight * 0.91
    print(newWeight)

elif number == 3:
    newWeight = weight * 0.38
    print(newWeight)

elif number == 4:
    newWeight = weight * 2.53
    print(newWeight)

elif number == 5:
    newWeight = weight * 1.07
    print(newWeight)

elif number == 6:
    newWeight = weight * 0.89
    print(newWeight)

elif number == 7:
    newWeight = weight * 1.14
    print(newWeight)

else:
    print("Invalid Number!")
