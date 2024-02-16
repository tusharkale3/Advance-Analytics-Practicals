import numpy as np

# 2D list
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)

# Convert into a numpy array
print(np.array(my_matrix))

# Now directly creating a 2D NumPy array

first = np.array([[1, 2, 3], [4, 5, 6]])
print(first)

second = np.array([[7, 8, 9], [10, 11, 12]])
print(second)

# 2 x 3
print(first.shape)

print(second.shape)

# Element by element addition
print(first + second)

# Add 1 to each element
print(first + 1)

print(first - 2)

print(first * 2)

print(first / 3)

print(first)

print(np.concatenate((first, second)))

print(np.concatenate((first, second), axis=1))

# Concatenate two single dimensional arrays
print(np.concatenate((np.array([1, 2, 3]), np.array([4, 5, 6]))))

# Concatenate two single dimensional arrays
# Error! 
# The np.concatenate function concatenates arrays along a specified axis. However, when dealing with 1-dimensional arrays, the axis parameter should be set to 0 (the default value) because there is only one axis (rows).

np.concatenate((np.array([1, 2, 3]), np.array([4, 5, 6])), axis=1)

# Ok now
np.concatenate((np.array([1, 2, 3]), np.array([4, 5, 6])), axis=0)