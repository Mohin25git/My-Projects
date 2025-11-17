# ----------------------------------------------
# 🧠 NumPy: Handling Missing or Infinite Values
# ----------------------------------------------
# Why do we care?
# In Machine Learning (ML), real-world data often has:
#   - Missing values (NaN = Not a Number)
#   - Infinite values (like division by zero, ∞)
# NumPy gives us tools to *detect and clean* these easily.
# ----------------------------------------------

import numpy as np

# 🧩 Step 1: Create an array with some missing (NaN) values
print("Original Array:")
arr = np.array([1, 2, np.nan, 4, np.nan, 6])
print(arr)

# 🕵️ Step 2: Detect Missing Values (NaN)
# np.isnan() checks each element:
# → True if value is NaN
# → False if it's a valid number
print("\nChecking for missing values (NaN):")
print(np.isnan(arr))

# ⚠️ You cannot directly compare NaN with anything — even itself!
print("\nCan NaN be compared to NaN directly?")
print(np.nan == np.nan)  # Always False, because NaN ≠ NaN by definition!

# 🧼 Step 3: Replacing NaN values using np.nan_to_num()
# Syntax: np.nan_to_num(array, nan=value)
# If 'nan' parameter is given → replaces NaN with that number.
# Default: replaces NaN with 0
print("\nReplacing missing values (NaN) with 100:")
cleaned_arr = np.nan_to_num(arr, nan=100)
print(cleaned_arr)

# If we don’t specify 'nan=value', NumPy replaces NaN with 0 by default.
print("\nReplacing missing values (NaN) with default (0):")
cleaned_default = np.nan_to_num(arr)
print(cleaned_default)

# ----------------------------------------------
# 🌌 Step 4: Working with Infinity
# ----------------------------------------------
# Infinite values appear when we divide by zero or have overflow.
# NumPy represents infinity as np.inf (positive) or -np.inf (negative)
print("\nCreating an array with Infinite values:")
New_Arr = np.array([2, 4, np.inf, 6, np.inf, 10])
print(New_Arr)

# 🧮 np.isinf() checks whether each element is infinite.
print("\nCheck which elements are Infinite (True = Infinite):")
print(np.isinf(New_Arr))

# 🚫 Step 5: Replacing Infinite Values
# np.nan_to_num() can also handle infinities:
#   - posinf → replaces +∞
#   - neginf → replaces -∞
print("\nReplacing positive and negative infinity with set limits:")
Nw_ARR = np.array([2, 4, np.inf, 8, -np.inf, 12])
cleaned_Arr = np.nan_to_num(Nw_ARR, posinf=1000, neginf=-1000)
print(cleaned_Arr)

# ----------------------------------------------
# ✅ Summary:
# np.isnan(x)      → Detects missing values
# np.isinf(x)      → Detects infinite values
# np.nan_to_num(x) → Cleans missing & infinite values
# ----------------------------------------------

# with AI