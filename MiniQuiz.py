# Import the random module to shuffle the quiz questions
import random as rd

# List of quiz questions
# Each question is a dictionary with:
#   - "question": the text of the question
#   - "options": a list of possible answers
#   - "answer": the correct answer
Questions = [
    {"question":"Who played Terminator(T-800)?", "options":["Arnold","Keanu","Dwayne"], "answer":"Arnold"},
    {"question":"Who is Albert Einstein?", "options":["Actor","Singer","Inventor"], "answer":"Inventor"},
    {"question":"What is Mohin's goal in life?", "options":["Accountant","Roboticist","Actor"], "answer":"Roboticist"},
    {"question":"Who is Mohin's competion?", "options":["Past-Self","Colleague","Enemy"], "answer":"Past-Self"},
    {"question":"Who is CEO of Nvidia?", "options":["Jenshen","Jeff","Elon"], "answer":"Jenshen"},
    {"question":"What is the fastest bike?", "options":["panigale-R","H2R","S1000RR"], "answer":"H2R"},
    {"question":"When was Transformers live-action released?", "options":["2003","2005","2007"], "answer":"2007"},
    {"question":"Who sang Same Old Love?", "options":["Taylor","Selena","Sabrina"], "answer":"Selena"}
]

# Shuffle the questions to randomize the order each time the quiz runs
rd.shuffle(Questions)

# Initialize the score counter
count = 0

# Loop through each question in the shuffled list
for Q in Questions:
    # Print the question text
    print(Q["question"])

    # Loop through the options and print them with numbers
    # enumerate() gives both an index (i) and the option text
    # start=1 ensures numbering starts from 1 for easier user selection
    for i, option in enumerate(Q["options"], 1):
        print(f"{i}.{option}")

    # Ask the user to input the number corresponding to their choice
    User_Choice = input("Enter the number of your choice: ")

    # Convert the input number to an index (subtract 1) and get the corresponding option text
    selected_option = Q["options"][int(User_Choice)-1]

    # Compare the selected option to the correct answer
    if selected_option == Q["answer"]:
        print("Correct choice!")   # Positive feedback for correct answer
        count += 1                 # Increment the score counter
        print("-" * 40)            # Separator for readability
    else:
        print(f"Wrong choice! The correct answer is {Q['answer']}")  # Feedback for wrong answer
        print("-" * 40)            # Separator for readability

# After all questions, print the final score
print(f"Your final score is {count}/{len(Questions)}")
