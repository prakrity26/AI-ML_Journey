import numpy as np

# Creating a 1D Array
arr = np.array([10, 20, 30, 40, 50])


# 1D Array Indexing

print(arr[0])      # First element -> 10
print(arr[2])      # Third element -> 30
print(arr[-1])     # Last element -> 50
print(arr[-2])     # Second last element -> 40



# 1D Array Slicing

print(arr[1:4])    # Elements from index 1 to 3 -> [20 30 40]
print(arr[:3])     # First 3 elements -> [10 20 30]
print(arr[2:])     # From index 2 to end -> [30 40 50]
print(arr[::2])    # Every 2nd element -> [10 30 50]
print(arr[::-1])   # Reverse the array -> [50 40 30 20 10]


# Creating a 2D Array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# 2D Array Indexing

print(matrix[0])       # First row -> [1 2 3]
print(matrix[1])       # Second row -> [4 5 6]
print(matrix[2])       # Third row -> [7 8 9]

print(matrix[0, 1])    # Row 0, Column 1 -> 2
print(matrix[1, 2])    # Row 1, Column 2 -> 6
print(matrix[2, 0])    # Row 2, Column 0 -> 7

# 2D Array Slicing

print(matrix[:, 0])    # First column -> [1 4 7]
print(matrix[:, 1])    # Second column -> [2 5 8]
print(matrix[:, 2])    # Third column -> [3 6 9]

print(matrix[0, :])    # First row -> [1 2 3]
print(matrix[1, :])    # Second row -> [4 5 6]
print(matrix[2, :])    # Third row -> [7 8 9]

print(matrix[0:2, :])  # First two rows
# [[1 2 3]
#  [4 5 6]]

print(matrix[:, 1:3])  # Last two columns
# [[2 3]
#  [5 6]
#  [8 9]]

print(matrix[1:, 1:])  # Bottom-right 2×2 submatrix
# [[5 6]
#  [8 9]]