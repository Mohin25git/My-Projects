# COUNT METHOD

# A dictionary storing student names and their grades
student_grades = {"mohin": "A", "tony": "A+", "elon": "A", "shyam": "B"}

# Extract only the grade values, convert to a list, and count how many times "A" appears
Result = list(student_grades.values()).count("A")
print(Result)   # prints: 2

# STRING COUNT METHOD

fruit_name = "-apple"

# Count how many times "p" appears inside the string
print(fruit_name.count("p"))  # prints: 2

# Show the original string
print(fruit_name)  # prints: -apple

# REPLACE METHOD

# Remove "-" from the string
result = fruit_name.replace("-", "")
print(result)  # prints: apple

# Replace "-ap" with "or", giving the funny transformation "-apple" → "orple"
resulT = fruit_name.replace("-ap", "or")
print(resulT)  # prints: orple

# MAKETRANS + TRANSLATE

Fruit = "mango"

# Create a translation table that replaces:
# 'm' → 't'
# 'a' → 'o'
res = Fruit.maketrans("ma", "to")

# Apply translation: "mango" → "tongo"
print(Fruit.translate(res))

# SPLIT METHOD

userName = "Mohin Shakya"

# Split breaks the string into a list of words
step1 = userName.split()
print(step1)  # ['Mohin', 'Shakya']

# Join the list back into a single string without spaces
print("".join(step1))  # MohinShakya

# REVERSE A SENTENCE

userInput = "I love south indian movies"

# Convert each word's first letter to uppercase
step_1 = userInput.title()
print(step_1)

# Split into a list for reversing
step2 = step_1.split()
print(step2)

# Reverse the list and join back into a sentence
print(" ".join(step2[::-1]))  # Reversed sentence

# USERNAME CLEANER (LOWERCASE CONVERTER)

fullName = input("Enter your full name: ")

# Convert to lowercase to standardize the username
clean = fullName.lower()

print(f"your username is: {clean}")

# PASSWORD SECRET CODE ENCRYPTER

password = "amazing_spiderman"

# Replace selected letters with symbols:
# a→@, e→3, i→!, o→0, s→$
stp1 = password.maketrans("aeios", "@3!0$")

# Apply the translation and append "0##9" just for effect
print(f"Your secret code is: {password.translate(stp1)}0##9")

# CLEANING AND EXTRACTING CLEAN USERNAME FROM EMAIL

email = "shakya.mohin416@gmail.com"

# Extract only the first 15 characters
cleaned1 = email[:15]

# Remove periods to get a continuous username
cleaned2 = cleaned1.replace(".", "")
print(cleaned2)  # prints: shakyamohin416

# PHONE NUMBER CLEANER – REMOVE +, -, AND SPACES

phoneNo = "+977 9847-366-756"

# make a translation table that deletes: '+', '-', and space (' ')
cleanUP = phoneNo.maketrans("", "", "+- ")

# apply the translation table to clean the phone number
cleaned = phoneNo.translate(cleanUP)

print(cleaned)  # prints: 9779847366756

#self Class
