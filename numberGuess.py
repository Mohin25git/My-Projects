import random as rd

number = rd.randint(1, 100)
attempts = 0

while True:
    Guess = int(input("Enter a number between(1-100): "))
    attempts += 1

    if Guess == number:
        print(f"Correct choice you guessed in {attempts} attempts!")
        break
    elif Guess < number:
        if number - Guess <= 5:
            print("Try a little higher, you are close!")
        else:
            print("Try higher!")
    else:
        if Guess - number <= 5:
            print("Try a little lower, you are close!")
        else:
            print("Try lower!")
