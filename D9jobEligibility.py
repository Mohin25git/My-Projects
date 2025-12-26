'''
Write a program to determine if a candidate is eligible for a job:  If the candidate's
age is >= 18, check if they have a degree. If they have a degree, check their work
experience: More than 3 years: Display "Highly Eligible." 1-3 years: Display
"Eligible." Less than 1 year: Display "Under Review.
'''
age = int(input("Enter your age: "))
degree = input("Do you have a degree?(yes/no): ").lower()
work_Experience = int(input("Enter your experience in years: "))

if age >= 18 and degree == "yes" and work_Experience > 3:
    print("Highly Eligible.")
elif age >= 18 and degree == "yes" and work_Experience <= 3:
    print("Eligible")
elif age >= 18 and degree == "yes" and work_Experience < 1:
    print("Under review")
else:
    print("In-eligible")
