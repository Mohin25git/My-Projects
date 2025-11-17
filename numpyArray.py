import numpy as np
arr = np.array([2, 4, 6, 8]) # When you have a list and you wanna convert it into numpy array
print(arr)

# creating Arrays with default values
zeroes_array = np.zeros(3)
print(zeroes_array)

ones_array =  np.ones((3, 4)) # Creates a 3 by 4 matrix array with 1 as the default value
print(ones_array)

# Full Function Array
full_array = np.full((4,4),8) # Creates an array with specific values you want in this case its 8
print(full_array)

# Creating sequences series of numbers
a_rr = np.arange(1,22, 2) # counts the numbers from 1 to 22 by skip of 2 steps or skipping 1 no each time
print(a_rr)

# Creating Identity Matrix
identity_matrix = np.eye(4) # Creates a 4 by 4 matrix with a diagonally running 1"s value
print(identity_matrix)

# self YT