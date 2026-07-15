# Import NumPy
import numpy as np


# Creating a 1D Array
arr = np.array([10, 20, 30, 40, 50])
print(arr)


# Creating a 2D Array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(matrix)


# Check Number of Dimensions
print(arr.ndim)
print(matrix.ndim)

# Check Total Number of Elements
print(arr.size)
print(matrix.size)


# Check Data Type
print(arr.dtype)


# Accessing Elements in 1D Array
print(arr[0])
print(arr[2])
print(arr[-1])


# Accessing Elements in 2D Array
print(matrix[0][1])
print(matrix[1][2])

# OR

print(matrix[0,1])
print(matrix[1,2])


# Slicing 1D Array
print(arr[1:4])


# Slicing 2D Array

# Second Column
print(matrix[:,1])

# Second Row
print(matrix[1,:])

# First Row
print(matrix[0,:])

# First Column
print(matrix[:,0])


# Modify Elements

# 1D Array
arr[2] = 100
print(arr)

# 2D Array
matrix[0,2] = 99
print(matrix)


# Creating Array of Zeros
zeros = np.zeros((2,3))
print(zeros)


# Creating Array of Ones
ones = np.ones((2,3))
print(ones)


# Creating Array using arange()
numbers = np.arange(1,10)
print(numbers)


# Reshape an Array
a = np.arange(1,7)

b = a.reshape(2,3)
print(b)


# Basic Arithmetic Operations
a = np.array([1,2,3])

print(a + 2)
print(a - 1)
print(a * 3)
print(a / 2)


# Operations Between Two Arrays
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# Useful Mathematical Functions
a = np.array([10,20,30,40])

print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))
print(np.sqrt(a))


# Transpose of a 2D Array
matrix = np.array([
    [1,2,3],
    [4,5,6]
])

print(matrix.T)

# Flatten a 2D Array
print(matrix.flatten())

# Iterate Through a 1D Array
for value in arr:
    print(value)


# Iterate Through a 2D Array
for row in matrix:
    print(row)


# Print Every Element of a 2D Array
for row in matrix:
    for value in row:
        print(value)


# Copy an Array
copy_array = arr.copy()
print(copy_array)


# Convert Python List to NumPy Array
mylist = [5,10,15,20]

array = np.array(mylist)

print(array)