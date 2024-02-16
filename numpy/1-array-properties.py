import numpy as np

nums_array = np.array([1, 2, 3, 4, 5])
print(nums_array)

print(type(nums_array))

print(nums_array[-1])

print(nums_array.shape)

print(nums_array.ndim)

print(nums_array.itemsize)

print(nums_array.size)

print(nums_array.dtype.name)

print(np.array([True, 10, 'abc', 5.5]))

print(np.array([True, 10, 'abc', 5.5]).dtype.name)