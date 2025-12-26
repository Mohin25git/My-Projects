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
replace1 = fruit_name.replace("-", "")
print(replace1)  # prints: apple

# Replace "-ap" with "or", giving the funny transformation "-apple" → "orple"
replace2 = fruit_name.replace("-ap", "or")
print(replace2)  # prints: orple

# MAKETRANS + TRANSLATE

Fruit = "mango"

# Create a translation table that replaces:
# 'm' → 't'
# 'a' → 'o'
replace3 = Fruit.maketrans("ma", "to")

# Apply translation: "mango" → "tongo"
print(Fruit.translate(replace3))

# SPLIT METHOD

userName = "Mohin Shakya"

# Split breaks the string into a list of words
step1 = userName.split()
print(step1)  # ['Mohin', 'Shakya']

# Join the list back into a single string without spaces
print("".join(step1))  # MohinShakya

# REVERSE A SENTENCE

sentence = "I love south indian movies"

# Convert each word's first letter to uppercase
step_1 = sentence.title()
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
transform = password.maketrans("aeios", "@3!0$")

# Apply the translation and append "0##9" just for effect
print(f"Your secret code is: {password.translate(transform)}0##9")

# CLEANING AND EXTRACTING CLEAN USERNAME FROM EMAIL

email = "shakya.mohin416@gmail.com"

# Extract only the first 15 characters
simplify_Mail = email[:15]

# Remove periods to get a continuous username
simpleMail = simplify_Mail.replace(".", "")
print(simpleMail)  # prints: shakyamohin416

# PHONE NUMBER CLEANER – REMOVE +, -, AND SPACES

phoneNo = "+977 9847-366-756"

# make a translation table that deletes: '+', '-', and space (' ')
cleanUP = phoneNo.maketrans("", "", "+- ")

# apply the translation table to clean the phone number
cleaned = phoneNo.translate(cleanUP)

print(cleaned)  # prints: 9779847366756

#self Class
