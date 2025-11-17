# -------------------------------------------------------------
# 🧠 NumPy Broadcasting: How NumPy Handles Arrays of Different Shapes
# -------------------------------------------------------------
# Broadcasting is NumPy’s superpower ⚡ — it lets you do math
# between arrays of *different shapes* automatically,
# without writing loops manually!
#
# 🧾 The Three Rules of Broadcasting:
# 1️⃣ Matching dimensions are added element-by-element (same length)
# 2️⃣ If one array has only one element, NumPy “expands” it across
#     the other array (like adding 10 to every element in [1,2,3])
# 3️⃣ Incompatible shapes (that don’t align in size) ❌ cause an error
#     Example: [1,2,3] + [1,2] → ❌
# -------------------------------------------------------------

import numpy as np   # Importing NumPy (our math assistant 🧮)

# -------------------------------------------------------------
# 💲 Example 1: Simple Discount Calculation
# -------------------------------------------------------------
print("🧾 The original array (Product Prices):")
prices = np.array([100, 200, 300])  # 3 product prices
print(prices)
# Output: [100 200 300]

# A flat 10% discount applies to all items.
discount = 10  # single number (scalar value)

print("\n💰 Prices after discount:")
# NumPy automatically broadcasts the single 'discount' value
# across the whole array — no loops needed!
FinalPrices = prices - (prices * discount / 100)
print(FinalPrices)
# Output: [90. 180. 270.]
# Explanation: Each element gets reduced by 10%

# -------------------------------------------------------------
# 🧩 Example 2: Matrix + Vector (Real Power of Broadcasting)
# -------------------------------------------------------------
print("\n🧮 Creating a new 2x3 matrix (think of it as 2 rows of 3 items each):")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])  # shape (2,3)
print(matrix)

print("\n🧾 Creating a 1D array (vector):")
vector = np.array([10, 20, 30])    # shape (3,)
print(vector)

# Let’s add them together!
# NumPy sees that the vector has 3 elements and the matrix has 3 columns.
# So it “broadcasts” the vector to both rows and performs element-wise addition.
print("\n✨ The result after broadcasting (matrix + vector):")
Result = matrix + vector
print(Result)
# Output:
# [[11 22 33]
#  [14 25 36]]

# -------------------------------------------------------------
# 🧠 What’s Happening Behind the Scenes:
# - NumPy automatically stretched (broadcasted) [10,20,30]
#   to match each row of the 2x3 matrix:
#   [[1,2,3],      +   [[10,20,30],
#    [4,5,6]]           [10,20,30]]
#
# - Then added corresponding elements → no loops required!
# -------------------------------------------------------------

# 🏁 Summary:
# Broadcasting makes NumPy ultra-efficient.
# It lets you perform operations between arrays of different shapes
# automatically, as long as their dimensions “line up”.
# -------------------------------------------------------------

# With AI
