
import numpy as np

# Create two arrays
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([2, 4, 5, 8])

# Display the arrays
print("First Array:", arr1)
print("Second Array:", arr2)

# Addition
print("\nAddition:", arr1 + arr2)

# Subtraction
print("Subtraction:", arr1 - arr2)

# Multiplication
print("Multiplication:", arr1 * arr2)

# Division
print("Division:", arr1 / arr2)

# Check array shapes
print("\nShape of First Array:", arr1.shape)
print("Shape of Second Array:", arr2.shape)

# Explain vectorized operations
print("\nVectorized Operations:")
print("NumPy performs calculations on all array elements at once.")
