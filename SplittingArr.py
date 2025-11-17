import numpy as np
'''
np.split()
equal

np.hsplit()
np.vsplit()
'''
print('The original array is:')
Arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(Arr)

print('splitting the array into 2:')
print(np.split(Arr, 2))

print('splitting the array into 4:')
print(np.split(Arr, 4))
