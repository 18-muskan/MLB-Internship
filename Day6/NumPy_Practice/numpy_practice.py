import numpy as np

# 1. Create a 1D array
one_d_array = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(one_d_array)

# 2. Create a 2D array
two_d_array = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n2D Array:")
print(two_d_array)

# 3. Arithmetic operations on arrays
array1 = np.array([10, 20, 30, 40])
array2 = np.array([1, 2, 3, 4])

print("\nArray 1:")
print(array1)

print("\nArray 2:")
print(array2)

print("\nAddition:")
print(array1 + array2)

print("\nSubtraction:")
print(array1 - array2)

print("\nMultiplication:")
print(array1 * array2)

print("\nDivision:")
print(array1 / array2)

# 4. Find maximum, minimum, mean, and sum
numbers = np.array([10, 20, 30, 40, 50])

print("\nNumbers:")
print(numbers)

print("\nMaximum:")
print(np.max(numbers))

print("\nMinimum:")
print(np.min(numbers))

print("\nMean:")
print(np.mean(numbers))

print("\nSum:")
print(np.sum(numbers))

# 5. Reshape an array
original_array = np.array([1, 2, 3, 4, 5, 6])

print("\nOriginal Array:")
print(original_array)

reshaped_array = original_array.reshape(2, 3)

print("\nReshaped Array (2 rows, 3 columns):")
print(reshaped_array)

# 6. Indexing
index_array = np.array([10, 20, 30, 40, 50])

print("\nIndexing:")
print("First element:", index_array[0])
print("Third element:", index_array[2])
print("Last element:", index_array[-1])

# 7. Slicing
print("\nSlicing:")
print("First three elements:", index_array[:3])
print("Elements from index 1 to 3:", index_array[1:4])
print("Last two elements:", index_array[-2:])

print("\nNumPy practice completed successfully!")