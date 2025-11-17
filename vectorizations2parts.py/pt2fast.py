# ----------------------------------------------------------
# 🧠 NumPy: Speeding Up Math Like a Pro
# ----------------------------------------------------------
# In this short program, we’ll explore two powerful NumPy concepts:
# 1️⃣ Broadcasting — automatically matching shapes for operations
# 2️⃣ Vectorization — performing operations on entire arrays at once (100x faster than loops!)
# ----------------------------------------------------------

import numpy as np   # Step 1: Importing NumPy — our math superhero 🦸‍♂️

# ----------------------------------------------------------
# 🧩 PART 1: Array Addition (Broadcasting)
# ----------------------------------------------------------
# Let's create two small arrays — think of them as two lists of numbers.
# NumPy can add them element-by-element instantly, no loops needed!

Arr1 = np.array([1, 2, 3])   # First array
Arr2 = np.array([4, 5, 6])   # Second array

# NumPy automatically lines them up and adds corresponding elements:
# [1+4, 2+5, 3+6] → [5, 7, 9]
result = Arr1 + Arr2         

print("Result of array addition:", result)
# Output: [5 7 9]

# ----------------------------------------------------------
# ⚙️ What happened here?
# NumPy performed **broadcasting**:
# It looked at both arrays, saw they are of the same shape (3 elements),
# and added each matching element together automatically.
# No need for any 'for' loops — pure vectorized speed! ⚡
# ----------------------------------------------------------

# ----------------------------------------------------------
# 🧩 PART 2: Multiplying Entire Array (Vectorization)
# ----------------------------------------------------------
# Here’s another array we’ll work with:
arr = np.array([10, 20, 30])

# Now we’ll multiply the entire array by 4.
# Instead of looping through each element manually,
# NumPy applies *the same operation* to every element instantly.
multiply = arr * 4

print("Array after multiplying by 4:", multiply)
# Output: [ 40  80 120]

# ----------------------------------------------------------
# ⚙️ What happened here?
# This is **vectorization**:
# - The single number “4” was “broadcasted” across the whole array.
# - So internally, NumPy did: [10*4, 20*4, 30*4]
# - All in one shot — super fast, super efficient.
# ----------------------------------------------------------

# ----------------------------------------------------------
# 🧾 SUMMARY:
# Broadcasting = NumPy automatically matches array shapes.
# Vectorization = One operation applies to the whole array instantly.
# Together, they make your math faster, simpler, and cleaner.
# ----------------------------------------------------------

# Self YT