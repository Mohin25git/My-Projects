'''
Write a Python program that:
Takes a student's marks (0–100) as input.
First checks if the student passed or failed.
Passing marks = 40
If the student passed, further classify them:

90–100 → Grade A

75–89 → Grade B

60–74 → Grade C

40–59 → Grade D

If the student failed (marks < 40), check:
If marks are 30–39 → “Failed, but eligible for re-exam.”
If marks are 0–29 → “Failed, needs to repeat the course.”
'''
marks = int(input("Enter your marks(0-100): "))

if marks >= 40:
    print("You have passed your exam!")
    if marks >= 90:
        print("Your grade is A")
    else:
        if marks >= 75:
            print("Your grade is B")
        else:
            if marks >= 60:
                print("Your grade is C")
            else:
                print("Your grade is D")
else:
    print("You have failed!")
    if marks >= 30:
        print("Failed, but eligible for re-exam!")
    else:
        print("Needs to retake the course!")

# # with elif version
# marks = int(input("Enter your marks(0-100): "))
# if marks >= 90:
#     print("grade A")
# elif marks >= 75:
#     print("grade B")
# elif marks >= 60:
#     print("grade C")
# elif marks >= 40:
#     print("grade D")
# elif marks >= 30:
#     print("Failed but eligible for re-exam")
# else:
#     print("Needs to retake the course")
