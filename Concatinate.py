'''
np.concatenate(array1, array2), axis = 0)

axis 0 > vertical stacking
axis 1 > horizontal stacking
'''
import numpy as np

print("Array 1 is:")
arr_1 = np.array([2,4,6,8])
print(arr_1)

print("Array 2 is:")
arr_2 = np.array([10,12,14,16])
print(arr_2)

print("New concatenated (added-up) array is:")
new_ARR = np.concatenate((arr_1, arr_2))
print(new_ARR)

# Self YT