import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0]) # Gives out first element
print(arr[2]) # Gives out third element
print(arr[-1]) # Goes behind the first element and gives out last element

# slicing: to abstract a portion of an array
arr2 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr2[1:5]) # index 1 to 5 i.e starts from second element to fifth
print(arr2[:4]) # index 0 to 3 i.e starts from 1st element to third
print(arr2[::2]) # every second element i.e from first and skips one element each time
print("Negative slicing:")
print(arr2[::-1]) # loops out and gives elements in reverse order "negative slicing"

# Fancy indexing
# taking the above "arr2"
print("Trying out fancy indexing: ")
print(arr2[[0, 2, 4]]) # 0: 10, 2: 30, 4: 50




