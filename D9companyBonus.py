'''
Ask the user for a subject score. If it's above 90, congratulate him. If it's between
50 and 90, suggest improvement. Otherwise, advise on retaking the course.
'''
score = int(input("Enter your score: "))
if score > 90:
    print("Great work! Congratulations.")

elif score >= 50 and score <= 90:
    print("needs more practice!")
    
else:
    print("retake the course!")
