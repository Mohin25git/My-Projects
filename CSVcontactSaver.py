#             CSV CONTACT SAVER PROGRAM
# This program allows the user to save multiple contacts
# (Name, Phone, Email) into a CSV file — which can later be
# opened easily in Excel, Google Sheets, or any text editor

import csv  # Importing the CSV module to handle CSV files

# Step 1️ — Set up the file name
file_name = "Contact.csv"

# Step 2️ — Ask the user how many contacts to store
no_of_contacts = int(input("Enter the number of contacts you want to save: "))

# Step 3️ — Open the CSV file in 'append' mode
#            (so it adds new data without deleting old ones)
with open(file_name, mode="a", newline="") as file:
    writer = csv.writer(file)  # Create a CSV writer object

    # Step 4️ — If the file is empty, write column headers first
    if file.tell() == 0:
        writer.writerow(["Name", "Phone", "Email"])

    # Step 5️ — Loop through and collect contact details
    for i in range(no_of_contacts):
        print(f"\nEnter details for Contact #{i+1}:")
        Name = input("Name: ")
        Phone = input("Phone: ")
        Email = input("Email: ")

        # Step 6️ — Write collected data into the CSV file
        writer.writerow([Name, Phone, Email])
        print(f"Contact '{Name}' saved successfully!")

# Step 7 — After saving all contacts, display confirmation message
print("\nAll contacts have been saved successfully into 'Contact.csv'!")
print("You can open this file in Excel, Notepad, Google Sheets, or any other text editor.")

# With AI