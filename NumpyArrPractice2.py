import numpy as np # NumPy = fast math engine for arrays & matrices

# Create a 3x3 matrix (think of this as a little data grid)
Ar1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(Ar1)

# SUM OF ALL ELEMENTS
# Adds every number inside Ar1 → gives one total value
Sum = np.sum(Ar1)
print("Total sum =", Sum)

# MEAN (AVERAGE) OF ALL ELEMENTS
# Finds the overall “average vibe” of the matrix
Mean = np.mean(Ar1)
print("Mean value =", Mean)

# ROW-WISE SUM
# axis=1 → move LEFT to RIGHT
# Gives the sum of each row separately
Row_Sum = np.sum(Ar1, axis=1)
print("Row-wise sum =", Row_Sum)

# COLUMN-WISE SUM
# axis=0 → move TOP to BOTTOM
# Gives the sum of each column separately
Col_Sum = np.sum(Ar1, axis=0)
print("Column-wise sum =", Col_Sum)

# MATRIX-WISE MEANS
# Same idea as sums, but now it’s averages (means)
np.mean(Ar1)            # mean of entire matrix
np.mean(Ar1, axis=1)    # mean of each row
np.mean(Ar1, axis=0)    # mean of each column

# CREATE ANOTHER MATRIX (Ar2) FILLED WITH ONES
# np.ones((3,3)) → creates a 3x3 matrix full of 1s
# Useful for testing addition/multiplication
Ar2 = np.ones((3,3))

# MATRIX ADDITION (Ar1 + Ar2)
# Adds corresponding elements together (simple element-wise add)
# Every value in Ar1 increases by 1
Ar3 = Ar1 + Ar2
print(Ar3)

# MATRIX MULTIPLICATION (Ar1 @ Ar2)
# "@" performs a real matrix multiplication:
# Row of Ar1 × Column of Ar2 = one cell in Ar4
# Used everywhere in robotics, AI, and transformations
Ar4 = Ar1 @ Ar2
print(Ar4)

# Self follow along with own-way
