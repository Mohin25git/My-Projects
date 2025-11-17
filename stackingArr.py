import numpy as np
'''
stacking: Vertically/Horizontally

vstack() Row-wise
hstack() Column-wise
'''
print('Array 1 is:')
Arr1 = np.array([2, 4 , 6, 8])
print(Arr1)

print('Array 2 is:')
Arr2 = np.array([10, 12, 14, 16])
print(Arr2)

print('vertically stacking two arrays:')
print(np.vstack((Arr1, Arr2)))

print('horizontally stacking two arrays:')
print(np.hstack((Arr1, Arr2)))
