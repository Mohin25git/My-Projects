import numpy as np
# filtering out a spiecific values
arr = np.array([10, 20, 30, 40, 50, 60])
print("output the values greater than 25: ")
print(arr[arr > 25])

''' Reshape (rows, columns) specify new shape 
if dimensions match
'''
arr2 = np.array([2, 4, 6, 8, 10, 12])
print("Reshaping the values into given dimension: ")
reshape_arr = arr.reshape(2,3)
print(reshape_arr)

# Self YT