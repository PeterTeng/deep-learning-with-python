import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([1.0, 0.5])
print(X)

W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3]) # Bias
print(W1)
print(B1)

print("A1 = XW1 + B1 = ")
A1 = np.dot(X, W1) + B1
print(A1)

Z1 = sigmoid(A1)
print("Z1 = ")
print(Z1)
