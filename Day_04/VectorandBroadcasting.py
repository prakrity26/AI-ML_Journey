import numpy as np
arr = np.array([1, 2, 3, 4])

print(arr + 10)        # adds 10 to every element, no loop needed
print(arr * 2)         # multiplies every element
print(arr ** 2)        # squares every element

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)            # element-wise addition

print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())
print(arr.std())        # standard deviation