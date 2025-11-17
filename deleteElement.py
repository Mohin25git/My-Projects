'''
np.delete(array, index, axis=None)
Flattened array
'''
import numpy as np

print("Original array:")
Arr = np.array([10, 20 , 30, 40, 50, 60, 70, 80])
print(Arr)

print("delete element function array:")
new_Arr = np.delete(Arr, 4, axis=None)
print(new_Arr)

# delete elements in 2D array
print("New 2D array:")
Arr_2D = np.array([[2,4,6],[8,10,12]])
print(Arr_2D)

print("Deleted index 1 in 2D array:")
New_Arr2D = np.delete(Arr_2D, 0, axis=0)
print(New_Arr2D)

# self YT