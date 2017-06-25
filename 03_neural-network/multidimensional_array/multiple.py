import numpy as np

# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# multiple = np.dot(A, B)

# print(multiple)

X = np.array([1.0, 0.5])
print(X)

W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3]) # Bias
print(W1)
print(B1)

print("XW + B = ")

Y = np.dot(X, W1) + B1

print(Y)
