import numpy as np

# check the shape of array when working with multi-dimentional data
arr_2d = np.array([[2, 4, 6],
                   [8, 9, 4]])
print("The shape of array is: ")
print(arr_2d.shape)

# Size checks the total number of elements in array
arr = np.array([[10, 20, 30], [40, 50, 60]])
print("The size of array is: ")
print(arr.size)

# Check the number of dimension
arr_1d = np.array([1, 2, 3])
arr_2D = np.array([[2, 4, 6], [6, 4, 8]])
arr_3d = np.array([[[2,4], [4,8], [8,9]]])

print("The dimension of array 1 is: ")
print(arr_1d.ndim) # ndim stands for number of dimension

print("The dimension of array 2 is: ")
print(arr_2D.ndim)

print("The dimension of array 3 is: ")
print(arr_3d.ndim)

# Check the datatype of array
aRr = np.array([10, 250.25, 22, 15])
print("The datatype of array is: ")
print(aRr.dtype) # dtype stands for datatype

# Covert the datatype to other type
Reeyy = np.array([1.2, 2.25, 3.10])
print("Converting into integer Matrix")
int_Reeyy = Reeyy.astype(int)

print(int_Reeyy)
print("Converted into integer: ")
print(int_Reeyy.dtype)
