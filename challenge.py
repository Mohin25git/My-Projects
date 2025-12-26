# # Ask user for full name in one input
# full_name = input("Enter your full name: ").strip()

# # Split the name into parts
# name_parts = full_name.split()

# # Extract first name and surname
# first = name_parts[0].lower()
# last = name_parts[-1].lower()

# # Combine with underscore
# final_name = first + "_" + last

# print(final_name)

fullName="Mohin Man Shakya"
step1=fullName.lower()
step2=step1.split()
step3='_'.join(step2)
print(step3)

name = "a123@asd"
# chars_remove="@"
step1 = name.maketrans("@", "")
print(step1.translate(name))
