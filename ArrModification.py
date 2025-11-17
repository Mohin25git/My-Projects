# --------------------------------------------------------------
# 🧠 Advanced NumPy: Understanding np.insert()
# --------------------------------------------------------------
# The np.insert() function helps you add (insert) new elements
# into an existing array — whether it’s a 1D or 2D array.
#
# Syntax:
#   np.insert(array, index, value, axis=None)
#
# 👉 array = the original array
# 👉 index = position where new data will be inserted
# 👉 value = actual value(s) to be inserted
# 👉 axis  = defines direction:
#       - If axis=None ➜ insertion happens in a flattened (1D) form
#       - axis=0 ➜ insert row-wise (for 2D arrays)
#       - axis=1 ➜ insert column-wise (for 2D arrays)
# --------------------------------------------------------------

import numpy as np   # Importing NumPy (the hero library for matrix operations)

# --------------------------------------------------------------
# 🧩 Step 1: Creating a 1D Array
# --------------------------------------------------------------
print("Original Array:")
arr = np.array([15, 20, 25, 30, 35, 40])  # A simple 1D array
print(arr)

# --------------------------------------------------------------
# 🧩 Step 2: Inserting a New Element into 1D Array
# --------------------------------------------------------------
# Let’s insert 100 into the 4th index (remember, indexing starts at 0)
# So positions are: 0→15, 1→20, 2→25, 3→30, 4→35...
# Inserting at index 4 means “place 100 before 35”
print("\nInserting new element at index 4:")
new_Arr = np.insert(arr, 4, 100)
print(new_Arr)
# Result: [15 20 25 30 100 35 40]

# --------------------------------------------------------------
# 🧩 Step 3: Creating a 2D Array
# --------------------------------------------------------------
# Now let’s level up! We’ll create a 2x2 matrix (2 rows, 2 columns)
print("\nCreating a new 2D array:")
arr2D = np.array([[1, 2],
                  [3, 4]])
print(arr2D)
# Output:
# [[1 2]
#  [3 4]]

# --------------------------------------------------------------
# 🧩 Step 4: Inserting a New Row
# --------------------------------------------------------------
# axis=0 → means row-wise insertion.
# index=1 → insert new row *after the first one* (rows count from 0)
print("\nRow-wise insertion:")
newArr2D = np.insert(arr2D, 1, [5, 6], axis=0)
print(newArr2D)
# Output:
# [[1 2]
#  [5 6]   <-- newly inserted row
#  [3 4]]

# --------------------------------------------------------------
# 🧩 Step 5: Inserting a New Column
# --------------------------------------------------------------
# axis=1 → means column-wise insertion.
# index=1 → insert new column between existing columns.
print("\nColumn-wise insertion:")
newArr_2D = np.insert(arr2D, 1, [5, 6], axis=1)
print(newArr_2D)
# Output:
# [[1 5 2]
#  [3 6 4]]

# --------------------------------------------------------------
# 🧩 Step 6: Flattening (axis=None)
# --------------------------------------------------------------
# axis=None means we treat the 2D array as a simple 1D line of numbers.
# So insertion happens in the flattened version.
print("\nFlattened insertion (axis=None):")
new_ARR2D = np.insert(arr2D, 1, [5, 6], axis=None)
print(new_ARR2D)
# Output: [1 5 6 2 3 4]
# The array got flattened first, then [5,6] were inserted at position 1.
# --------------------------------------------------------------

# ✅ Summary:
# - axis=0 → add a new ROW
# - axis=1 → add a new COLUMN
# - axis=None → insert into a flat version (1D)
# --------------------------------------------------------------

# Self YT
