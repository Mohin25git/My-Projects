import random as rd

result = rd.randrange(0,5)
rangeNo = int(input("enter the range number: "))

if result == 0:
    print("Flamingo turn pink from eating shrimp.")

elif result == 1:
    print("The only food that doesnt spoil is honey.")

elif result == 2:
    print("A tastebuds lifespan is abolut 10 days.")

elif result == 3:
    print('it is impossible to sneeze while sleeping.')

elif result == 4:
    print("its illegal to sing off-key in North Korea.")

else:
    print("Invalid")
