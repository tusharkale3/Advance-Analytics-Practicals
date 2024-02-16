import numpy as np

# Random numbers
print(np.random.rand(2))

print(np.random.rand(5,5))

# Random numbers as per the normal distribution - Values closer to 0 appear
print(np.random.randn(2))

print(np.random.randn(5,5))

# Random integers only
print(np.random.randint(1,100,10))

# Seed to reproduce the "random" numbers
np.random.seed(42)
print(np.random.rand(4))

np.random.seed(1)
print(np.random.randint(10, 20, size=(4,5)))

print("Repeat?")
np.random.seed(1)
print(np.random.randint(10, 20, size=(4,5)))

# Seed value is generated automatically
print(np.random.uniform(10.0, 50.0, size=(3,3)))

print("Repeat?")

# Seed value is generated automatically
print(np.random.uniform(10.0, 50.0, size=(3,3)))