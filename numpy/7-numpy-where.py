import numpy as np

# Create a random array
arr = np.random.randint(0, 100, 10)

# Filter values based on a condition
condition = arr > 50
result = np.where(condition)

print("Original Array:", arr)
print("Indices where value > 50:", result)
print("Filtered Values:", arr[result])

# Create two random arrays
arr1 = np.random.randint(0, 10, 5)
arr2 = np.random.randint(10, 20, 5)

# Combine values from two arrays based on a condition
condition = arr1 > 5
result = np.where(condition, arr1, arr2)

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Combined Array based on condition:", result)
