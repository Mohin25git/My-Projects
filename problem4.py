import os

# Specify the directory you want to list
directory = "."  # "." means current directory

try:
    # List all files and folders in the directory
    contents = os.listdir(directory)
    
    print(f"Contents of '{directory}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory}'.")
